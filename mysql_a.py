# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
import pymysql

db = pymysql.connect(host="127.0.0.1", user="root", password="123", port=3306, db="bookschina")
cur = db.cursor()
'''
cur.execute("DROP TABLE IF EXISTS EP")  
SQL = """CREATE TABLE EP(  
         first_name CHAR(20) NOT NULL,
         age INT,
         income float)"""  # 创建表

cur.execute(SQL)
'''

# sql_insert = """insert into ep(first_name,age,income) values('zhoucy','25','18000')"""
# sql_insert = """update ep set first_name='%s' where age='%d'"""
# cur.execute(sql_insert)
# cur.execute(sql_insert % ("hang", 24))
# db.commit()
# db.close()
sql_inserts = """ select * from bookchina1 """
cur.execute(sql_inserts)

results = cur.fetchall()
# print(results)
for row in results:
    sname = row[0]
    sage = row[1]
    sincome = row[2]
    print(sname, sage, sincome)

db.commit()
db.close()


