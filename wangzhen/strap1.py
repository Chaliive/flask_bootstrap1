# -*- coding:utf-8 -*-
from flask import Flask, request, render_template
import pymysql
import psutil
import datetime
import time

current_user = ['登录']
db = pymysql.connect(host='192.168.195.177', user='wz', password='123', db='mytest', port=3306)
cur = db.cursor()

app = Flask(__name__)


@app.route('/index')
def show_post():
    if current_user[-1] != '登录':
        cpu_num = psutil.cpu_count(logical=False)  # 物理 CPU 个数
        cpu_use = str(psutil.cpu_percent(1))  # cpu使用率
        free = str(round(psutil.virtual_memory().free / (1024 * 1024 * 1024), 2))  # 空闲内存数
        total = str(round(psutil.virtual_memory().total / (1024 * 1024 * 1024), 2))  # total:物理内存大小
        memory = int(psutil.virtual_memory().total - psutil.virtual_memory().free) / float(
            psutil.virtual_memory().total)  # 内存利用率

        net = psutil.net_io_counters()  # 获取网络读写字节／包的个数
        sent = net.bytes_recv / 1024 / 1024

        user_count = len(psutil.users())  # 用户个数
        user_list = ",".join([u.name for u in psutil.users()])  # 用户列表

        pid = []
        psids = psutil.pids()  # 所有进程ID
        for psid in psids:
            pid_info = []
            p = psutil.Process(psid)
            pid_info.append(p.name())
            pid_info.append(p.memory_percent())
            pid_info.append(p.status())
            pid_info.append(p.create_time())
            pid.append(pid_info)

        diskinfo = psutil.disk_partitions()  # 磁盘分区信息
        d = []

        for i in diskinfo:
            disk_info = []
            info = psutil.disk_usage(i.device)
            d_total = str(int(info.total / (1024 * 1024 * 1024)))
            disk_info.append(d_total)
            d_used = str(int(info.used / (1024 * 1024 * 1024)))
            disk_info.append(d_used)
            d.append(disk_info)
        disk_num = len(diskinfo)  # 磁盘总数
        local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        insert_sys = """
        insert into sys(cpu_num,cpu_use,free,total,memory,sent,user_count,disk_num,local_time) values(%s,%s,%s,%s,%s,%s,%s,%s,str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'))
        
        """ % (cpu_num, cpu_use, free, total, memory, sent, user_count, disk_num, local_time)
        cur.execute(insert_sys)
        db.commit()

        select_new5 = """
         select cpu_use,free,memory,local_time from sys order by local_time desc limit 5
        """
        cur.execute(select_new5)
        sys_result = cur.fetchall()
        sys_info = []
        for row in sys_result:
            a = [row[0], row[1], row[2], row[3]]
            sys_info.append(a)

        return render_template('common/echart_show.html', cpu_num=cpu_num, cpu_use=cpu_use, free=free, \
                               memory=memory, total=total, disk_num=disk_num, diskinfo1=d[0], diskinfo2=d[1],
                               diskinfo3=d[2], diskinfo4=d[3], diskinfo5=d[4], \
                               sent=sent, user_list=user_list, user_count=user_count, pid=pid[0], time=sys_info,
                               user=current_user[-1])
    else:
        return render_template('common/login.html', user=current_user[-1])


@app.route('/regist')
def regist():
    return render_template('common/regist.html', user=current_user[-1])


@app.route('/regist', methods=['POST'])
def regist_post():
    nickname = request.form['username']
    rename = """
    select * from regist where nickname='%s'
    """
    n = cur.execute(rename % nickname)
    db.commit()
    if n > 0:
        return render_template('common/regist.html', user="昵称已被使用")
    else:
        password = request.form['pwd']
        email = request.form['email']
        phone = request.form['tel']
        sql_insert = """
    insert into regist values('%s','%s','%s','%s')
    """
        cur.execute(sql_insert % (nickname, password, email, phone))
        db.commit()
        return render_template('common/login.html', user=current_user[-1])


@app.route('/login', methods=['GET'])
def login():
    return render_template('common/login.html', user=current_user[-1])


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
            cpu_num = psutil.cpu_count(logical=False)  # 物理 CPU 个数
            cpu_use = str(psutil.cpu_percent(1))  # cpu使用率
            free = str(round(psutil.virtual_memory().free / (1024 * 1024 * 1024), 2))  # 空闲内存数
            total = str(round(psutil.virtual_memory().total / (1024 * 1024 * 1024), 2))  # total:物理内存大小
            memory = int(psutil.virtual_memory().total - psutil.virtual_memory().free) / float(
                psutil.virtual_memory().total)  # 内存利用率

            net = psutil.net_io_counters()  # 获取网络读写字节／包的个数
            sent = net.bytes_recv / 1024 / 1024

            user_count = len(psutil.users())  # 用户个数
            user_list = ",".join([u.name for u in psutil.users()])  # 用户列表

            pid = []
            psids = psutil.pids()  # 所有进程ID
            for psid in psids:
                pid_info = []
                p = psutil.Process(psid)
                pid_info.append(p.name())
                pid_info.append(p.memory_percent())
                pid_info.append(p.status())
                pid_info.append(p.create_time())
                pid.append(pid_info)

            diskinfo = psutil.disk_partitions()  # 磁盘分区信息
            d = []

            for i in diskinfo:
                disk_info = []
                info = psutil.disk_usage(i.device)
                d_total = str(int(info.total / (1024 * 1024 * 1024)))
                disk_info.append(d_total)
                d_used = str(int(info.used / (1024 * 1024 * 1024)))
                disk_info.append(d_used)
                d.append(disk_info)
            disk_num = len(diskinfo)  # 磁盘总数
            local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            insert_sys = """insert into sys(cpu_num,cpu_use,free,total,memory,sent,user_count,disk_num,local_time) 
            values(%s,%s,%s,%s,%s,%s,%s,%s,str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s')) 
            
            """ % (cpu_num, cpu_use, free, total, memory, sent, user_count, disk_num, local_time)
            cur.execute(insert_sys)
            db.commit()

            select_new5 = """
             select cpu_use,free,memory,local_time from sys order by local_time desc limit 5
            """
            cur.execute(select_new5)
            sys_result = cur.fetchall()
            sys_info = []
            for row in sys_result:
                a = []
                a.append(row[0])
                a.append(row[1])
                a.append(row[2])
                a.append(row[3])
                sys_info.append(a)
            return render_template('common/echart_show.html', cpu_num=cpu_num, cpu_use=cpu_use, free=free,
                                   memory=memory, total=total, disk_num=disk_num, diskinfo1=d[0], diskinfo2=d[1],
                                   diskinfo3=d[2], diskinfo4=d[3], diskinfo5=d[4],
                                   sent=sent, user_list=user_list, user_count=user_count, pid=pid[0], time=sys_info,
                                   user=current_user[-1])
    return render_template('common/login.html', mess='用户名或密码不正确', user=current_user[-1])


app.run(host='127.0.0.1', port=999, debug=True)

db.close()
