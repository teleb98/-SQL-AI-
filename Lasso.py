#pymysql 연동해서  db="lasso"에 접속
#Lasso 회귀 모델을 학습하고 회귀선을 시각화 및 성능 평가

import pymysql
con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='n0w10s01!!',
    db='regression_model',
    charset='utf8mb4'
)
cursor=con.cursor(pymysql.cursors.DictCursor)

sql_select = "select * from hw_200"
cursor.execute(sql_select)
result = cursor.fetchall()
for i in result:
    print(i['Height(Inches)"'], i['"Weight(Pounds)"'])

con.close()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

#데이터프레임 생성
df = pd.DataFrame(result)
print(df)

# 데이터프레임에서 Height(Inches)와 Weight(Pounds) 컬럼 추출
x = df['Height(Inches)"']
y = df['"Weight(Pounds)"']

#Lasso 회귀 모델 학습
model = Lasso()
model.fit(x.values.reshape(-1, 1), y)

#학습된 Lasso 회귀 모델의 기울기와 절편
print('기울기:', model.coef_)
print('절편:', model.intercept_)
print('결정계수:', model.score(x.values.reshape(-1, 1), y))

#학습된 Lasso 회귀 모델의 예측값
y_pred = model.predict(x.values.reshape(-1, 1))
print(y_pred)


#학습된 Lasso 회귀 모델의 MSE, RMSE
mse = mean_squared_error(y, y_pred)
print('MSE:', mse)
print('RMSE:', np.sqrt(mse))

#학습된 Lasso 회귀 모델의 회귀선 시각화
plt.scatter(x, y, label='data')
plt.plot(x, y_pred, color='red', label='Lasso regression')
plt.legend()

plt.show()

