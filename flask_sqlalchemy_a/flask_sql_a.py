# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# 写配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
# 设置每次请求结束后会自动提交数据库的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


# 表
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    ro1 = Role(id=1, name='zhou', email='123@.qq.com')  # 类的实例化并传入数据
    db.session.add(ro1)
    db.session.commit()
    # 增
    ro2 = Role(id=2, name='li', email='334@qq.com')
    ro3 = Role(id=3, name='yang', email='789@qq.com')
    ro4 = Role(id=4, name='yue', email='852@qq.com')
    db.session.add_all([ro2, ro3, ro4])
    db.session.commit()
    # 查
    r1 = db.session.query(Role).filter_by(id=1).first()
    # r1 = Role.query.first()
    print(r1.email)
    # 改
    # r2 = db.session.query(Role).filter_by(id=2).first()
    # r2.name = "zhang"
    # db.session.commit()
    # # print(r2.name)
    # # 删
    # r3 = db.session.query(Role).filter_by(id=3).first()
    # db.session.delete(r3)
    # db.session.commit()
    # Role.query.all()


