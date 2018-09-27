# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import pymysql
# from flask_system_orm.scratch_data import user_list, pro_res

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='bookschina', port=3306, charset='utf8')
    cur = conn.cursor()  # 使用cursor()方法获取操作游标
    sql = "SELECT * FROM bookchina1"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('index.html', u=u, user_list=user_list, pro_res=pro_res)


if __name__ == '__main__':
    app.run()

