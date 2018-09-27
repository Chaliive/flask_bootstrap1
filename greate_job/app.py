# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
import time
import os  # subprocess
import pymysql
from flask import Flask, request
from flask import render_template
from greate_job.calcu import process, memory, cpu, disk, net
from greate_job import ad, test
current_user = ['登录']
app = Flask(__name__)
db = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test', port=3306)
cur = db.cursor()  # 对数据库进行增删改查


def add_data():
    mmr_info = memory()
    cpu_time = cpu()
    e_net = net()
    io_disk = disk()['io']
    # print(cpu_time[1], cpu_time[0], mmr_info[1], mmr_info[0], mmr_info[2], mmr_info[3], io_disk[0], io_disk[1], e_net[0], e_net[1])
    insert_sys = """insert into monitor(sys_time,cpu_per,total_mem,free_mem,used_mem,mem_per,io_read,io_write,
    net_sent, net_recv) values('%s','%f','%f','%f','%f','%f','%f','%f','%f','%f')"""
    cur.execute(insert_sys % (
        cpu_time[1], cpu_time[0], mmr_info[1], mmr_info[0], mmr_info[2], mmr_info[3], io_disk[0], io_disk[1], e_net[0],
        e_net[1]))
    db.commit()


def get_data():
    select_sys = """
             select cpu_per,free_mem,mem_per,sys_time from monitor order by id desc limit 10
            """  # 取后10组数据
    cur.execute(select_sys)
    sys_result = cur.fetchall()
    # print(sys_result)
    return sys_result  # resutl是一个包含元组的元组


@app.route('/storage_ctrl')
def index():
    while True:
        time.sleep(5)
        add_data()
        sys_result = get_data()
        info = memory()
        pro_res = process()
        return render_template('storage_ctrl.html', sys_result=sys_result, info=info, pro_res=pro_res)


@app.route('/performance')
def index2():
    while True:
        time.sleep(5)
        add_data()
        sys_result = get_data()
        info = memory()
        pro_res = process()
        return render_template('performance.html', s=sys_result, info=info, pro_res=pro_res)


@app.route('/regist')
def regist():
    return render_template('regist.html', user=current_user[-1])


@app.route('/regist', methods=['POST'])
def regist_post():
    nickname = request.form['username']
    rename = """
    select * from regist where nickname='%s'
    """
    n = cur.execute(rename % nickname)
    db.commit()
    if n > 0:
        return render_template('regist.html', user="昵称已被使用")
    else:
        info = memory()
        password = request.form['pwd']
        email = request.form['email']
        phone = request.form['tel']
        sql_insert = """
    insert into regist values('%s','%s','%s','%s')
    """
        cur.execute(sql_insert % (nickname, password, email, phone))
        db.commit()
        return render_template('login.html', user=current_user[-1], info=info)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', user=current_user[-1])


@app.route('/login', methods=['POST'])
def login_form():
    sql_select = """
select nickname,password from regist
"""
    cur.execute(sql_select)
    db.commit()
    results = cur.fetchall()
    for row in results:
        if request.form['username'] == row[0] and request.form['pwd'] == row[1]:
            username = request.form['username']
            current_user.append(username)
            info = memory()
            sys_result = get_data()
            pro_res = process()
            return render_template('storage_ctrl.html', info=info, sys_result=sys_result, pro_res=pro_res)
    return render_template('login.html', mess='用户名或密码不正确', user=current_user[-1])


@app.route('/zabbix', methods=['GET', 'POST'])
def zabbix_get():
    ip = request.form['ip']
    username = request.form['username']
    pwd = request.form['pwd']
    content = request.form['content']
    zbx_url = "http://" + ip + "/zabbix/api_jsonrpc.php"
    zabbix_user = username
    zabbix_pwd = pwd
    token = ad.get_token(zbx_url, zabbix_user, zabbix_pwd)
    info = test.zbx_req(content, token)
    info = info[0]
    return render_template('zabbix.html', info=info)


@app.route('/s', methods=['GET', 'POST'])
def zabbix():
    return render_template('zabbix.html')


@app.route('/', methods=['GET'])
def fabric():
    return render_template('fabric.html')


@app.route('/fabric', methods=['GET', 'POST'])
def fabric_get():
    command = request.form['command']
    print(command)
    strr = os.popen("fab -H localhost " + command + " -f fab_1.py").read()  # 注意localhost和-f之间的空格
    print(strr)
    return render_template('fabric.html', strr=strr)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5401, debug=True)
