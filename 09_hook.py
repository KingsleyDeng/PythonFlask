# coding:utf-8

from flask import Flask, make_response, jsonify, request, session

app = Flask(__name__)


@app.route("/index")
def index():
    print("index被执行")
    return "index page"


@app.route("/hello")
def hello():
    print("hello 被执行")
    return "hello page"


@app.before_first_request
def handle_before_first_request():
    """在第一次请求处理之前 先被执行"""
    print("handle_before_first_request 被执行")


@app.before_request
def handler_before_request():
    """在每次请求之前都被执行"""
    print("handler_before_request 被执行")


@app.after_request
def handler_after_request(response):
    """在每次请求（视图函数处理）之后都被执行,前提是视图函数没有出现异常"""
    print("handler_after_request 被执行")
    return response


@app.teardown_request
def handler_teardown_request(response):
    """在每次请求之后都被执行， 无论视图函数是否出现异常都被执行"""
    print("handler_teardown_request 被执行")
    return response


if __name__ == '__main__':
    app.run(debug=True)
