# -*- coding:utf-8 -*-
from flask import Flask, render_template
from flask import request
import pymysql
from conda.cli.main_clean import execute
from random import randint

app = Flask(__name__)
db = pymysql.connect('localhost', 'root', '123456', 'test1')
cur = db.cursor()


@app.route('/login', methods=['GET'])
def login():
    return render_template('bootstrap/login.html')


@app.route('/login', methods=['POST'])
def index():
    semail = request.form['email']
    spasswd = request.form['password']
    sql = """ select email,passwd from zhuce where email='%s' and passwd='%s' """ % (semail, spasswd)
    cur.execute(sql)
    results = cur.fetchone()
    if results:
        db1 = pymysql.Connection('localhost', 'root', '123456', 'test')
        cur1 = db1.cursor()
        sql_shuju = """ select name,salary_min,salary_max,job_address,work_years,Enducation,job_type,job_advantage,job_bts,field from lagou ORDER BY RAND() limit 5"""
        cur1.execute(sql_shuju)
        results = cur1.fetchall()
        db1.commit()
        print(results)
        return render_template('bootstrap/boke.html', u=results)
        db.close()
        db1.close()
    else:
        return render_template('bootstrap/login.html', message='密码或账号错误', )
        db.close()


@app.route('/zhuce', methods=['POST'])
def zhuce():
    return render_template('bootstrap/zhuce.html')


@app.route('/', methods=['POST'])
def zhu():
    sname = request.form['first_name']
    slast = request.form['last_name']
    email1 = request.form['email']
    passwd = request.form['password']
    sql_yan = """ select email from zhuce where email='%s'""" % (email1)
    cur.execute(sql_yan)
    emails = cur.fetchone()  # none
    if not emails:
        sql_cun = """ insert into zhuce(first_name, last_name, email, passwd) values('%s', '%s', '%s', '%s') """
        cur.execute(sql_cun % (sname, slast, email1, passwd))
        db.commit()
        return render_template('bootstrap/login.html')
    else:
        return render_template('bootstrap/zhuce.html', message='邮箱已注册')
    db.close()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('bootstrap/cuowu.html'), 404


app.run(debug=True)
