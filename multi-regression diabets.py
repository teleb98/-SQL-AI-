import pymysql
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# pymysql 연동해서 db="diabetic_data"에 접속
con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='n0w10s01!!',
    db='diabetic_data',
    charset='utf8mb4'
)
cursor = con.cursor(pymysql.cursors.DictCursor)

sql_select = "SELECT * FROM diabetic_data"
cursor.execute(sql_select)
result = cursor.fetchall()

con.close()

# 데이터프레임 생성
df = pd.DataFrame(result)

# '?' 값을 NaN으로 대체
df.replace('?', np.nan, inplace=True)

# 문자열 데이터가 아닌 컬럼에 대해서만 평균을 계산하여 NaN을 대체
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# 원-핫 인코딩으로 'age' 컬럼 변환
df = pd.get_dummies(df, columns=['age'])
df = pd.get_dummies(df, columns=['weight'])

# # 'weight' 컬럼과 원-핫 인코딩된 'age' 컬럼들을 특성으로 사용
# x_columns = ['weight'] + [col for col in df if col.startswith('age_')]
# x = df[x_columns]
# y = df['patient_nbr']

# print(df.columns)

# # 다중 회귀 모델 학습
# model = LinearRegression()
# model.fit(x, y)

# # 학습된 다중 회귀 모델의 기울기, 절편 및 결정계수 출력
# print('기울기:', model.coef_)
# print('절편:', model.intercept_)
# print('결정계수:', model.score(x, y))

# # 학습된 다중 회귀 모델의 예측값
# y_pred = model.predict(x)

# # MSE 및 RMSE 계산 및 출력
# mse = mean_squared_error(y, y_pred)
# print('MSE:', mse)
# print('RMSE:', np.sqrt(mse))

# # 학습된 다중 회귀 모델의 회귀선 시각화
# plt.scatter(df['weight'], y, label='data')
# plt.plot(df['weight'], y_pred, color='red', label='linear regression')
# plt.legend()
# plt.show()

# 원-핫 인코딩된 'age' 및 'weight' 컬럼들을 특성으로 사용
x_columns = [col for col in df.columns if col.startswith('age_') or col.startswith('weight_')]
x = df[x_columns]
y = df['patient_nbr']

print(df.columns)

# 다중 회귀 모델 학습
model = LinearRegression()
model.fit(x, y)

# 학습된 다중 회귀 모델의 기울기, 절편 및 결정계수 출력
print('기울기:', model.coef_)
print('절편:', model.intercept_)
print('결정계수:', model.score(x, y))

# 학습된 다중 회귀 모델의 예측값
y_pred = model.predict(x)

# MSE 및 RMSE 계산 및 출력
mse = mean_squared_error(y, y_pred)
print('MSE:', mse)
print('RMSE:', np.sqrt(mse))

# 시각화 부분은 수정이 필요합니다. 다중 회귀 모델의 시각화는 복잡할 수 있으므로, 
# 여기서는 예시로 'age_'로 시작하는 첫 번째 컬럼을 사용합니다.
first_age_column = [col for col in df.columns if col.startswith('age_')][0]
plt.scatter(df[first_age_column], y, label='data')
plt.plot(df[first_age_column], y_pred, color='red', label='linear regression')
plt.legend()
plt.show()
