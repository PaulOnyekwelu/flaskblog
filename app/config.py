from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app import app

app.secret_key = 'gdfght6y79uhg54'
path = "mysql://root:root@localhost/flask_blog"
app.config['SQLALCHEMY_DATABASE_URI'] = path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(20), unique=True, nullable=False)
    cat_url = db.Column(db.String(20), unique=True, nullable=False)
    date_added = db.Column(db.DateTime)
    # post = db.Column(db.relationship("Post", backref="category"))

    def __init__(self, cat_name, cat_url, date):
        self.cat_name = cat_name
        self.cat_url = cat_url
        self.date_added = date


class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(20), unique=True, nullable=False)
    post = db.relationship("Post", backref="author")

    def __init__(self, name):
        self.name = name


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_author = db.Column(db.Integer, db.ForeignKey("admin.admin_id"))
    post_title = db.Column(db.String(255), nullable=False)
    post_content = db.Column(db.Text, nullable=False)
    post_date = db.Column(db.DateTime)
    post_cat = db.Column(db.Integer, db.ForeignKey("category.cat_id"))

    def __init__(self, author, title, content, date, cat):
        self.post_author = author
        self.post_title = title
        self.post_content = content
        self.post_date = date
        self.post_cat = cat


@app.errorhandler(404)
def page_not_found(e):
    title = '404 page not found'
    return render_template('404.html', title=title), 404


@app.errorhandler(500)
def internal_server_error(e):
    title = 'internal_server_error'
    return render_template('500.html', title=title), 500
