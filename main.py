# coding:utf-8

from flask import Flask
from goods import get_goods
from users import register
# 循环引用 解决方法 推迟一方的导入 让另一方先完成


app = Flask(__name__)

app.route("/get_goods")(get_goods)
app.route("/register")(register)

@app.route("/")
def index():
    return "index page"

if __name__ == '__main__':
    print(app.url_map)
    app.run()
