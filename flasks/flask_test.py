# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


# @app.route('/', methods=['POST', 'GET'])
# def home():
#     return '<h1>welcome!!</h1>'


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    if request.form['username'] == 'admin' and request.form['password'] == '123':
        #     return render_template('login.html', username='successful!!!')
        # return render_template('login.html', message='error', username='username')
        return render_template('login2.html')
    return render_template('login2.html')


app.run(host='127.0.0.1', port=5401, debug=True)


