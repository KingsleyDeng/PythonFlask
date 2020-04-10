# coding:utf-8

from flask import Flask, make_response, jsonify, request

app = Flask(__name__)


@app.route("/set_cookie")
def index():
    resp = make_response("success")
    # 设置Cookie，默认有效期是临时cookie 浏览器关闭即失效
    resp.set_cookie("Itcast", "Python")
    resp.set_cookie("Itcast", "Python", max_age=3600)
    # 响应头中设置Cookie
    # resp.headers["Set-Cookie"]
    return resp


# 获取Cookie
@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("Itcast")
    return c


@app.route("/delete_cookie")
def del_cookie():
    resp = make_response("del success")
    # 删除cookie
    resp.delete_cookie("Itcast")
    return resp


if __name__ == '__main__':
    app.run(debug=True)
