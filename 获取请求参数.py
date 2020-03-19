# coding utf-8
# __author__:KingsleyDeng

from flask import Flask, request

app = Flask(__name__)


@app.route("/indexs", methods=["GET", "POST"])
def index():
    # request 中包含了前端发送过来的所有请求数据
    # form和data是用来提取请求体参数
    # request.form 可以直接提取请求体中的表单格式的数据
    # 通过get方式只能拿到多个同名参数的第一个
    name = request.form.get("name")
    age = request.form.get("age")
    print("request.data: %s" %request.data)
    # args是用来提取url中的参数（查询字符串）
    city = request.args.get("city")
    return "hello name=%s, age=%s, city=%s" % (name, age, city)

if __name__ == '__main__':
    app.run(debug=True)
