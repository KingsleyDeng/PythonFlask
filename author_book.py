# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/author_book_py04"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "dsvqrvzvc"


app.config.from_object(Config)

db = SQLAlchemy(app)


# 定义数据库的模型
class Author(db.Model):
    """作者"""
    __tablename__ = "tbl_authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship("Book", backref="author")


class Book(db.Model):
    """书籍"""
    __tablename__ = "tbl_books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))


# 创建表单模型类
class AuthorBookForm(FlaskForm):
    """作者数据表单模型类"""
    author_name = StringField(label="作者", validators=[DataRequired("作者必须填写")])
    book_name = StringField(label="书籍", validators=[DataRequired("书籍必须填写")])
    submit = SubmitField(label="提交")


@app.route("/", methods=["GET", "POST"])
def index():
    # 创建表单对象
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证表单成功
        # 提取表单数据
        author_name = form.author_name.data
        book_name = form.book_name.data
        # 保存数据
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        db.session.add(book)
        db.session.commit()

    # 查询数据库
    authors_li = Author.query.all()
    print(authors_li)
    return render_template("author_book.html", authors=authors_li, form=form)


@app.route("/delete_book", methods=["POST"])
def delete_book():
    """删除书籍"""
    # 提取参数
    # 如果前端发送的请求体数据是json get_json会解析成字典
    # get_json 要求前端传送的数据的Content-Type：application/json
    req_dict = request.get_json()
    book_id = req_dict.get("book_id")

    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return jsonify(code=0, message="OK")


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # au_xi = Author(name="我吃西红柿")
    # au_qian = Author(name="萧潜")
    # au_san = Author(name="唐家三少")
    # db.session.add_all([au_xi, au_qian, au_san])
    # db.session.commit()
    #
    # bk_xi = Book(name="吞噬星空",author_id=au_xi.id)
    # bk_xi2 = Book(name="寸芒",author_id=au_qian.id);
    # bk_qian = Book(name="飘邈之旅",author_id=au_qian.id)
    # bk_san = Book(name="冰火魔厨",author_id=au_san.id)
    # db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
    # db.session.commit()
    app.run(debug=True)
