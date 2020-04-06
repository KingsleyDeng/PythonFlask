from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login():
    # name = request.form.get("")
    # pwd = request.form.get("")

    name = ""
    pwd = ""

    if name != "zhangsan" and pwd != "admin":
        # abort函数立即终止视图函数的执行
        # 可以返回给前端特定的信息
        # 1. 传递状态码信息（*必须是标准的HTTP状态码）
        # 2. 传递响应体信息
        resp = Response("Login Fail")
        abort(resp)
        # 执行其他的操作代码

    return "Login Success"


# 定义错误处理的方法
@app.errorhandler(404)
def handle_404_error(error):
    """自定义处理错误方法"""
    # 这个函数的返回值会是前端用户看到的最终结果
    return u"出现了404错误，错误信息%s" % error


if __name__ == '__main__':
    app.run(debug=True)
