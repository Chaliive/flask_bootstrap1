# -*- coding:utf-8 -*-
import sqlite3
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


def get_db():
    db = sqlite3.connect('mydb.db')
    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    rv = cur.fetchall()
    db.close()
    return (rv[0] if rv else None) if one else rv


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/cpu", methods=["POST"])
def cpu():
    if request.method == "POST":
        res = query_db("SELECT * FROM cpu WHERE id>=(?)", args=(int(request.form['id']) + 1,))  # 返回1+个数据

    return jsonify(insert_time=[x[1] for x in res],
                   cpu1=[x[2] for x in res],
                   cpu2=[x[3] for x in res],
                   cpu3=[x[4] for x in res],
                   cpu4=[x[5] for x in res])  # 返回json格式


if __name__ == "__main__":
    app.run(debug=True)
