# coding:utf-8
import json

from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route("/index")
def index():
    # json 就是字符串
    data = {
        "name": "python",
        "age": 18
    }
    # json模块中的dumps方法 将python字典转换为json字符串
    # json loads 方法 将python字符串转换为json字典
    #
    # json_str = json.dumps(data)
    #
    # return json_str,200,{"Content-Type":"application/json"}
    # jsonify 帮助转为json数据 并设置响应头Content-Type 为Application/Json
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
