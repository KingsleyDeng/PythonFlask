from flask import Flask

__author__ = '精神小伙'

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])


@app.route('/hello')
def hello():
    # 基于类的视图（即插视图）
    return 'HELLO WORLD KINGSLEY'


# app.add_url_rule('/hello', view_func=hello)


# 程序的入口文件
if __name__ == "__main__":
    # 生产环境 nginx+uwsgi
    app.run(host="192.168.2.104", debug=app.config['DEBUG'], port=81)
