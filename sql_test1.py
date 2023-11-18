#pymysql 연동해서  db="traffic_accident"에 접속
import pymysql
con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='n0w10s01!!',
    db='traffic_accident',
    charset='utf8mb4'
)
cursor=con.cursor(pymysql.cursors.DictCursor)

sql_select = "select * from accident order by 사고건수 DESC"
cursor.execute(sql_select)
result = cursor.fetchall()
for i in result:
    print(i["사고건수"], i["사고유형"])

con.close()