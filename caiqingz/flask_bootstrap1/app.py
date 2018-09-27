from flask import Flask
from flask import request, render_template
import pymysql

app = Flask(__name__)
db = pymysql.connect("localhost", "root", "123", "test")
cursor = db.cursor()


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_POST():
    username = request.form['username']
    password = request.form['password']
    sql = "select * from user_info where username='%s'" % (username)
    cursor.execute(sql)
    date = cursor.fetchall()
    for row in date:
        if row[1] == password:
            return render_template('JD.html')
    return render_template('login.html', message=True)


@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_POST():
    username = request.form['username']
    password = request.form['password']
    sql = "select * from user_info where username='%s'" % (username)
    cursor.execute(sql)
    date = cursor.fetchone()
    if date == None:
        sql = '''insert into login(username,password) values(%s,%s)'''
        cursor.execute(sql, (username, password))
        db.commit()
        return render_template('login.html', flag=True)

    return render_template('signup.html', Flag=True)


if __name__ == '__main__':
    app.run(debug=True)
