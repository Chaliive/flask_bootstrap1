# -*- coding: utf-8 -*-
from flask import Flask, render_template
import os
from teach_model.exts import db
from teach_model.models import Role

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

# 设置每次请求结束后会自动提交数据库的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)


def create_db():
    db.drop_all()
    db.create_all()

    r1 = Role(name='zhou', email='this is test')
    r2 = Role(name='chuang', email='this is  a n')
    db.session.add_all([r1, r2])
    db.session.commit()


def select_db():
    pass


def add_db():
    pass


def delete_db():
    pass


def update_db():
    pass


@app.route('/createdb')
def first():
    create_db()
    return "WLCOME FEICUI IN BEIJNG "


@app.route('/list')
def first():
    select_db()
    return render_template('login.html', me='ipgd')


@app.route('/add')
def first():
    select_db()
    return render_template('one.html', me='ads')


@app.route('/delete')
def first():
    select_db()
    return render_template('one.html', me='abcd')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=778, debug=True)
