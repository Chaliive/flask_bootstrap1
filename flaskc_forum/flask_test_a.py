# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
import pymysql
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


# @app.route('/', methods=['POST', 'GET'])
# def home():
#     return '<h1>welcome!!</h1>'


@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/', methods=['POST'])
def login_post():
    if request.form['username'] == 'admin' and request.form['password'] == '123':
        #     return render_template('login.html', username='successful!!!')
        # return render_template('login.html', message='error', username='username')
        return render_template('forum.html')
    return render_template('login.html', message='用户名或密码错误')


@app.route('/register', methods=['GET'])
def register():
    return render_template('regist.html')
    # if request.form['new'] == request.form['']


@app.route('/registerUser')
def getRegister():
    db = pymysql.connect("localhost", "root", "123", "test")
    cursor = db.cursor()
    username = request.args.get('username')
    password = request.args.get('oldpwd')
    sql = """insert into user_info(username,password) values('%s', '%s')"""
    cursor.execute(sql % (username, password))
    db.commit()
    db.close()
    return render_template('login.html')
# db.close()


app.run(host='127.0.0.1', port=5401, debug=True)



