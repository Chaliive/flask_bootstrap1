# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
from flask_system_orm.exts import db


class Info(db.Model):
    __tablename__ = 'info'
    mem_total = db.Column(db.String, primary_key=True)
    mem_free = db.Column(db.Float)
    mem_used = db.Column(db.Float)
    mem_percent = db.Column(db.Float)


class Progress(db.Model):
    __tablename__ = 'progress'
    pro_name = db.Column(db.String(64), primary_key=True)
    pro_sta = db.Column(db.String(64), index=True)
    pro_gid = db.Column(db.String(64))
    pro_par = db.Column(db.String(64))
    p = db.Column(db.String(64))
