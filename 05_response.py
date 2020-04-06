from flask import Flask, make_response

app = Flask(__name__)


@app.route("/index")
def index():
    # 1 使用元祖 返回自定义的响应信息
    #       响应体     状态码     响应头
    # return "index page", 400, [("Itcast", "python"), ("City", "武汉")]

    # 使用make_response 来构造响应信息
    resp = make_response("index page 2")
    # 设置状态码
    resp.status = "999 itcast"
    # 设置响应头
    resp.headers["city"] = "wuhan"
    return resp


if __name__ == '__main__':
    app.run(debug=True)
