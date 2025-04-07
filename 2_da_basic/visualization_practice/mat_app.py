import streamlit as st
import pandas as pd 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns 
import matplotlib.font_manager as fm 


# 한글폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic' 
plt.rcParams['axes.unicode_minus'] = False 
sns.set(font='Malgun Gothic', 
        rc={'axes.unicode_minus' : False}, 
        style='darkgrid')

# 페이지 설정
st.set_page_config(page_title="Matplotlib & Seaborn 튜토리얼", layout="wide") 
st.title("Matplotlib & Seaborn 튜토리얼") 

# 데이터셋 불러오기 
tips = sns.load_dataset('tips') 

# 데이터 미리보기 
st.subheader('데이터 미리보기')
st.dataframe(tips.head())

# 기본 막대 그래프, matplotlit + seaborn 
st.subheader("1. 기본 막대 그래프")
# 객체지향방식으로 차트 작성
# 그래프를 그리는 목적 : (예쁘게)잘 나오라고
fig, ax = plt.subplots(figsize=(10, 6)) # matplotlib

sns.barplot(data=tips, x='day', y='total_bill', ax=ax) # seaborn

ax.set_title('요일별 평균 지불 금액')
ax.set_xlabel('요일') 
ax.set_ylabel('평균 지불 금액($)')

# plt.show() ==> 이 문법은 jupyter notebook, google colab에서 사용
st.pyplot(fig) # streamlit 문법

# 산점도
# x축, y축이 연속형 변수여야 합니다.
st.subheader('2. 산점도')
fig1, ax1 = plt.subplots(figsize=(10, 6)) # matplotlib

sns.barplot(data=tips, x='day', y='total_bill', ax=ax) # seaborn
sns.scatterplot(data = tips, x = 'total_bill', y = 'tip', 
                hue='day', ax = ax1)
st.pyplot(fig1)

# 히트맵
st.subheader("3. 히트맵")

# 요일과 시간별 평균 팁 계산
pivot_df = tips.pivot_table(values='tip', index='day', columns='time',
                            aggfunc='mean')
fig2, ax2 = plt.subplots(figsize = (10, 6))
sns.heatmap(pivot_df, annot=True, fmt='.2f', ax = ax2)
st.pyplot(fig2)

# 회귀선이 있는 산점도
st.subheader("4. 회귀선이 있는 산점도")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.regplot(data = tips, x = 'total_bill', y = 'tip',
            scatter_kws = {'alpha':0.5,}, ax = ax3)
st.pyplot(fig3)

# gpt 팁 fig, ax = plt.subplots() 이런방식으로 만들어달라

st.subheader("5. 요일별 팁의 분포 (Boxplot)")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='tip', ax=ax4)
ax4.set_title("요일별 팁의 분포")
st.pyplot(fig4)

st.subheader("6. 성별에 따른 총지불 금액 분포 (Violinplot)")
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.violinplot(data=tips, x='sex', y='total_bill', ax=ax5)
ax5.set_title("성별에 따른 총지불 금액 분포")
st.pyplot(fig5)

st.subheader("7. 흡연자 / 비흡연자 수")
fig6, ax6 = plt.subplots(figsize=(8, 5))
sns.countplot(data=tips, x='smoker', hue='sex', ax=ax6)
ax6.set_title("성별에 따른 흡연자 / 비흡연자 수")
st.pyplot(fig6)

st.subheader("8. 전체 변수 간 관계 보기 (Pairplot)")
st.markdown("💡 이 plot은 시간이 조금 걸릴 수 있습니다.")
sns_plot = sns.pairplot(tips, hue='sex')
st.pyplot(sns_plot.fig)

st.subheader("9. 요일 + 시간 조합별 총지불금액 분포")
g = sns.FacetGrid(tips, row='day', col='time', height=4)
g.map_dataframe(sns.histplot, x='total_bill', bins=10)
st.pyplot(g.fig)

st.subheader("10. 변수 간 상관관계 히트맵")
corr = tips.corr(numeric_only=True)
fig7, ax7 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax7)
ax7.set_title("상관관계 히트맵")
st.pyplot(fig7)