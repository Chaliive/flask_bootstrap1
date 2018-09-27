# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018
# @Author:Chaliive
# @Email: zhoucy567@qq.com
# @Note
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import pymysql, time, os
from flask_system_orm.scratch_data import scratch_memory, scratch_prograss
from flask_system_orm.exts import db
from flask_system_orm import storage


app = Flask(__name__)
bootstrap = Bootstrap(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)


def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    # db.session.close()


# error #
def add_db():
    info = scratch_memory()
    mem_total = info['mem_total']
    mem_free = info['mem_free']
    mem_used = info['mem_used']
    mem_percent = info['mem_percent']
    db.session.add_all([mem_total, mem_free, mem_used, mem_percent])
    print([mem_total, mem_free, mem_used, mem_percent])
    db.session.commit()


@app.route('/')
def index():
    # create_db()
    # storage.Info()
    # add_db()
    while True:
        time.sleep(10)
        info = scratch_memory()
        pro_res = scratch_prograss()
        return render_template('show.html', info=info, pro_res=pro_res)


# @app.route('/')
# def index():
#     while True:
#         time.sleep(10)
#         info = scratch_memory()
#         pro_res = scratch_prograss()
#         return render_template('show.html', info=info, pro_res=pro_res)


if __name__ == '__main__':
    app.run()
