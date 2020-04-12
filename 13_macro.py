# coding:utf-8

from flask import Flask, render_template, flash

app = Flask(__name__)
flag = True

app.config["SECRET_KEY"] = "fasdfafa"

@app.route("/index")
def index():
    if flag:
        # 通过flask添加闪现信息
        flash("hello 1")
        flash("hello 2")
        flash("hello 3")
        global flag
        flag = False

    return render_template("macro.html")


if __name__ == '__main__':
    app.run(debug=True)
