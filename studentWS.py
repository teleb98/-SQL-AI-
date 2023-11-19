# student 웹 서비스 연동 코드

import pymysql
from flask import Flask, jsonify
app = Flask(__name__)

def get_db():
    con=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='n0w10s01!!',
        db='students',
        charset='utf8mb4'
    )
    return con

con = get_db()

@app.route('/students')
def get_student():
    cursor=con.cursor(pymysql.cursors.DictCursor)
    sql_select = "select * from students"
    cursor.execute(sql_select)
    rows = cursor.fetchall()
    students = []
    for i in rows:
        student = {
            "id": i["id"],
            "name": i["name"],
            "age": i["age"],
            "major": i["major"]
        }
        students.append(student)
    return jsonify(students)

app.run(port=5000, debug=True)