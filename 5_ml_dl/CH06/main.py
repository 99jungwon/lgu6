import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import lightgbm as lgb
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='lightgbm')

# 데이터 로딩
print("Loading data...")
train = pd.read_csv("train.csv")

# 특성 선택
missing_ratio = train.isnull().mean()
drop_cols = missing_ratio[missing_ratio > 0.3].index.tolist() + ['id']

numeric_feats = train.select_dtypes(include=['int64', 'float64']).columns.tolist()
corr = train[numeric_feats].corr()['SalePrice'].abs().sort_values(ascending=False)
main_numeric = corr[corr > 0.3].index.tolist()
main_categorical = ['Neighborhood', 'ExterQual', 'KitchenQual', 'BsmtQual', 'GarageType', 'SaleCondition']

main_features = list(set(main_numeric + main_categorical) - set(drop_cols))
X = train[main_features]
y = train['SalePrice']

numeric_feats = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_feats = X.select_dtypes(include=['object']).columns.tolist()

# 파이프라인 정의
numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_feats),
    ('cat', categorical_transformer, categorical_feats)
])

# 모델 정의
models = {
    'Ridge': Ridge(),
    'Lasso': Lasso(),
    'ElasticNet': ElasticNet(),
    'XGBoost': xgb.XGBRegressor(tree_method='hist', random_state=42),
    'LightGBM': lgb.LGBMRegressor(random_state=42, verbose=-1)
}

results = {}

# 모델 학습 및 평가
for name, model in models.items():
    print(f"\nTraining model: {name}")

    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', model)
    ])

    pipe.fit(X, y)
    y_pred = pipe.predict(X)

    rmse = np.sqrt(mean_squared_error(y, y_pred))
    print(f"Completed {name}, RMSE: {rmse:.4f}")

    results[name] = rmse

print("\nFinal Results:")
results_df = pd.DataFrame(results.items(), columns=['Model', 'RMSE']).sort_values(by='RMSE')
print(results_df)