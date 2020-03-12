# -- coding: UTF-8 --

from flask import Flask
app = Flask(__name__)

@app.route("/index")
def index():
    return "Hello Index"

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()