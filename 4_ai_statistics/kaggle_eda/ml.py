import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from sklearn.ensemble import VotingRegressor
from datetime import datetime

# 데이터 로딩
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# 피처 엔지니어링 추가 (BMI, Intensity, Weight_Duration_Interaction)
def add_features(df):
    df['BMI'] = df['Weight'] / (df['Height']/100)**2
    df['Intensity'] = df['Heart_Rate'] * df['Duration']
    # 새로운 피처: 몸무게와 운동 시간의 상호작용
    df['Weight_Duration_Interaction'] = df['Weight'] * df['Duration']
    # 새로운 피처: 심박수 제곱 (비선형 관계 포착)
    df['Heart_Rate_Sq'] = df['Heart_Rate']**2
    return df

train = add_features(train)
test = add_features(test)

# 원-핫 인코딩 (Sex)
train = pd.get_dummies(train, columns=['Sex'], drop_first=True) # drop_first=True로 한 컬럼만 남기기 (다중공선성 방지)
test = pd.get_dummies(test, columns=['Sex'], drop_first=True)

# 'Sex_female' 컬럼이 없는 경우를 대비 (테스트 데이터에 없을 수 있음)
if 'Sex_female' not in train.columns:
    train['Sex_female'] = 0
if 'Sex_female' not in test.columns:
    test['Sex_female'] = 0

# 특성 정의 - 새로운 피처들 포함
features = ['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp', 
            'BMI', 'Intensity', 'Weight_Duration_Interaction', 'Heart_Rate_Sq', 'Sex_female'] # Sex_male 대신 Sex_female 사용

# 타겟 변수 로그 변환
y = np.log1p(train['Calories'])

# 특성 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(train[features])
test_scaled = scaler.transform(test[features])

# 데이터 분할
X_tr, X_val, y_tr, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 개별 모델 정의 (random_state 설정)
xgb = XGBRegressor(random_state=42)
lgb = LGBMRegressor(random_state=42, n_jobs=-1) # n_jobs=-1로 병렬 처리
cat = CatBoostRegressor(random_state=42, verbose=0,  # verbose=0으로 학습 과정 출력 제거
                        early_stopping_rounds=50) # 과적합 방지를 위한 early stopping 추가

print("--- XGBoost 하이퍼파라미터 튜닝 시작 ---")
# 최적의 하이퍼파라미터 튜닝 (XGBoost 기준) - GridSearchCV 범위 확장
params_xgb = {
    'n_estimators': [200, 400, 600], # 추정기 개수 증가
    'max_depth': [4, 6, 8], # 트리의 최대 깊이 증가
    'learning_rate': [0.01, 0.03, 0.05], # 학습률 조정
    'subsample': [0.7, 0.9], # 각 트리에 사용할 샘플의 비율
    'colsample_bytree': [0.7, 0.9] # 각 트리에 사용할 피처의 비율
}

grid_xgb = GridSearchCV(xgb, params_xgb, scoring='neg_mean_squared_error', cv=5, n_jobs=-1, verbose=1) # cv=5로 교차 검증 횟수 증가, n_jobs=-1로 병렬 처리
grid_xgb.fit(X_tr, y_tr)

best_xgb = grid_xgb.best_estimator_
print("XGBoost 최적 하이퍼파라미터:", grid_xgb.best_params_)
print("--- XGBoost 하이퍼파라미터 튜닝 완료 ---\n")

print("--- LightGBM 하이퍼파라미터 튜닝 시작 ---")
# LightGBM 하이퍼파라미터 튜닝 예시 (실제로는 더 넓은 범위 탐색)
params_lgb = {
    'n_estimators': [200, 400, 600],
    'learning_rate': [0.01, 0.03, 0.05],
    'num_leaves': [20, 31, 40], # 트리의 복잡성 제어
    'max_depth': [-1, 6, 8] # -1은 제한 없음
}
grid_lgb = GridSearchCV(lgb, params_lgb, scoring='neg_mean_squared_error', cv=5, n_jobs=-1, verbose=1)
grid_lgb.fit(X_tr, y_tr)
best_lgb = grid_lgb.best_estimator_
print("LightGBM 최적 하이퍼파라미터:", grid_lgb.best_params_)
print("--- LightGBM 하이퍼파라미터 튜닝 완료 ---\n")


print("--- CatBoost 하이퍼파라미터 튜닝 시작 ---")
# CatBoost 하이퍼파라미터 튜닝 예시 (실제로는 더 넓은 범위 탐색)
params_cat = {
    'iterations': [200, 400, 600], # n_estimators와 유사
    'learning_rate': [0.01, 0.03, 0.05],
    'depth': [4, 6, 8], # 트리의 깊이
    'l2_leaf_reg': [1, 3, 5] # L2 정규화 강도
}
grid_cat = GridSearchCV(cat, params_cat, scoring='neg_mean_squared_error', cv=5, n_jobs=-1, verbose=1)
grid_cat.fit(X_tr, y_tr)
best_cat = grid_cat.best_estimator_
print("CatBoost 최적 하이퍼파라미터:", grid_cat.best_params_)
print("--- CatBoost 하이퍼파라미터 튜닝 완료 ---\n")


# 앙상블 모델 구성 - 튜닝된 최적 모델과 가중치 부여
# 각 모델의 검증 성능에 따라 가중치를 조절해 보세요.
# 예: xgb (0.4), lgb (0.3), cat (0.3)
ensemble = VotingRegressor(estimators=[
    ('xgb', best_xgb),
    ('lgb', best_lgb),
    ('cat', best_cat)
], weights=[0.4, 0.3, 0.3], n_jobs=-1) # n_jobs=-1로 병렬 처리

print("--- 앙상블 모델 학습 시작 ---")
ensemble.fit(X_tr, y_tr)
print("--- 앙상블 모델 학습 완료 ---")

# 평가
y_pred = ensemble.predict(X_val)

def rmsle(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

print("앙상블 검증 RMSLE:", rmsle(y_val, y_pred))

# 최종 예측 및 제출
final_pred = np.expm1(ensemble.predict(test_scaled)) # 로그 변환 되돌리기

# 음수 예측값 처리 (칼로리는 음수가 될 수 없음)
final_pred[final_pred < 0] = 0

submission = pd.DataFrame({
    'id': test['id'],
    'Calories': final_pred
})

now = datetime.now().strftime("%Y%m%d_%H%M%S")
submission.to_csv(f'submission_{now}.csv', index=False)
print(f"제출파일 생성 완료: submission_{now}.csv")