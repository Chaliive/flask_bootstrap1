# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
# 导入数据库模块
import pymysql
# 导入Flask框架，这个框架可以快捷地实现了一个WSGI应用
from flask import Flask
# 默认情况下，flask在程序文件夹中的templates子文件夹中寻找模块
from flask import render_template
# 导入前台请求的request模块
from flask import request
import traceback

# 传递根目录
app = Flask(__name__)


# 默认路径访问登录页面
@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')


# 默认路径访问注册页面
@app.route('/regist', methods=['GET'])
def regist():
    return render_template('regist.html')


# # 设置响应头
# def Response_headers(content):
#     resp = Response(content)
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     return resp


# 获取注册请求及处理
@app.route('/registuser', methods=['POST'])
def getRigistRequest():
    # 把用户名和密码注册到数据库中

    # 连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect("localhost", "root", "123", "test")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # print(cursor)
    # username = request.from('user')
    username = request.args.get('user')
    password = request.args.get('password')
    # SQL 插入语句
    # sql = "INSERT INTO user_info(username, password) VALUES (" + request.args.get('user') + ", " + request.args.get(
    #     'password') + ")"
    sql = """insert into user_info(username,password) values('%s', '%s')"""
    print(request.args.get('user'), request.args.get('password'))
    # print(sql)
    # sql = """insert into ep(first_name,age,income) values('zhoucy','25','18000')"""
    try:
        # 执行sql语句
        cursor.execute(sql % (username, password))
        # 提交到数据库执行
        db.commit()
        # 注册成功之后跳转到登录页面
        return render_template('login.html')
    except:
        # 抛出错误信息
        traceback.print_exc()
        # 如果发生错误则回滚
        db.rollback()
        return '注册失败'
    # 关闭数据库连接
    db.close()


# 获取登录参数及处理
@app.route('/login', methods=['POST'])
def getLoginRequest():
    # 查询用户名及密码是否匹配及存在
    # 连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect("localhost", "root", "123", "test")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    username = request.args.get('user')
    password = request.args.get('password')
    # SQL 查询语句
    # sql = "select * from username where username=" + request.args.get('user') + " and password=" + request.args.get(
    #     'password') + ""
    sql = """select * from user_info where username='%s' and password='%s'"""
    print(request.args.get('user'), request.args.get('password'))
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql % (username, password))
        results = cursor.fetchall()
        print(len(results))
        print(results)
        if len(results) == 1:
            return '登录成功'
        else:
            return '用户名或密码不正确'
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()


# 使用__name__ == '__main__'是 Python 的惯用法，确保直接执行此脚本时才
# 启动服务器，若其他程序调用该脚本可能父级程序会启动不同的服务器
if __name__ == '__main__':
    app.run(debug=True)

"""改变了post/get方法"""
