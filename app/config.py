from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app import app

app.secret_key = 'hello from silanka'
path = "mysql://root:root@localhost/flask_blog"
app.config['SQLALCHEMY_DATABASE_URI'] = path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(20), unique=True)
    cat_url = db.Column(db.String(20), unique=True)
    date_added = db.Column(db.DateTime)

    def __init__(self, cat_name, cat_url, date):
        self.cat_name = cat_name
        self.cat_url = cat_url
        self.date_added = date


@app.errorhandler(404)
def page_not_found(e):
    title = '404 page not found'
    return render_template('404.html', title=title), 404


@app.errorhandler(500)
def internal_server_error(e):
    title = 'internal_server_error'
    return render_template('500.html', title=title), 500
