# -- coding: UTF-8 --

from flask import Flask
from flask import url_for
from flask import redirect

app = Flask(__name__)


@app.route("/index")
def index():
    return "Hello Index"


@app.route("/")
def hello():
    return "Hello Worlds!"


@app.route('/user/<username>')
def show_user_profile(username): \
        # show the user profile for that user
    return 'User %s' % username


# int 接受整数
# float 接受浮点数
# path 和缺省情况一样，但也可以接受斜杠
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/test')
def test_url_for():
    url = url_for("hello")
    return redirect(url)



if __name__ == "__main__":
    app.debug = True
    app.run()
