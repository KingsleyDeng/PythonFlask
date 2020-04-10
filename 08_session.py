# coding:utf-8

from flask import Flask, make_response, jsonify, request, session

app = Flask(__name__)
# flask的session需要用到秘钥
app.config["SECRET_KEY"] = "asdfasd"

# flask 默认把session保存到cookie中

@app.route("/login")
def login():
    # 设置session数据
    session["name"] = "Python"
    session["mobile"] = "12312312319"
    return "login success"


@app.route("/index")
def index():
    # 获取session数据
    name = session.get("name")
    return "Hello %s" % name


if __name__ == '__main__':
    app.run(debug=True)
