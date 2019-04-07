from app import app
from flask import render_template, url_for
from app.config import Category


# front page routing
@app.route('/')
def home():
    title = 'Home Page'
    cat = Category.query.all()

    return render_template('public/index.html', title=title, category=cat)


@app.route('/about')
def about():
    title = 'About'
    return render_template('public/about.html', title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Login Page'
    return render_template('public/login.html', title=title)


@app.route('/reset-password')
def forgot():
    title = 'Password Reset'
    return render_template('public/forgot.html', title=title)


@app.route("/category/<cat_id>")
def cat(cat_id):
    return render_template("public/cat.html")
