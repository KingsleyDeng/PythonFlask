# coding:utf-8

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        "name": "python",
        "age": 18,
        "my_dict": {"city": "wh"},
        "my_list": [1, 2, 3, 4, 5],
        "my_int": 0
    }

    return render_template("index.html", **data)


# 自定义的过滤器
def list_step_2(li):
    """以步长为2的自定义过滤器"""
    return li[::2]

# 自定义的过滤器
@app.template_filter("list3")
def list_step_3(li):
    """以步长为2的自定义过滤器"""
    return li[::3]

# 注册过滤器
app.add_template_filter(list_step_2,"list2")


if __name__ == '__main__':
    app.run(debug=True)
