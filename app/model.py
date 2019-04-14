from app import db, login_manager
from flask_login import UserMixin


class Category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(20), unique=True, nullable=False)
    cat_url = db.Column(db.String(20), unique=True, nullable=False)
    date_added = db.Column(db.DateTime)
    post = db.relationship("Post", backref="category", lazy=True)

    def __init__(self, cat_name, cat_url, date):
        self.cat_name = cat_name
        self.cat_url = cat_url
        self.date_added = date


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin_full_name = db.Column(db.String(20))
    admin_username = db.Column(db.String(20), unique=True, nullable=False)
    admin_email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(70))
    post = db.relationship("Post", backref="author", lazy=True)

    def __init__(self, name, username, email, password):
        self.admin_full_name = name
        self.admin_username = username
        self.admin_email = email
        self.password = password


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_author = db.Column(db.Integer, db.ForeignKey("admin.id"))
    post_title = db.Column(db.String(255), nullable=False)
    post_content = db.Column(db.Text, nullable=False)
    post_date = db.Column(db.DateTime)
    post_cat = db.Column(db.Integer, db.ForeignKey("category.cat_id"))
    comment = db.relationship("Comment", backref="post", lazy=True)

    def __init__(self, author, title, content, date, cat):
        self.post_author = author
        self.post_title = title
        self.post_content = content
        self.post_date = date
        self.post_cat = cat


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, db.ForeignKey("post.post_id"))

    def __init__(self, name, email, content, post, date):
        self.name = name
        self.email = email
        self.content = content
        self.post_id = post
        self.date = date
