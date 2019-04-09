from app import app
from flask import render_template, url_for
from app.model import Category


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


@app.errorhandler(404)
def page_not_found(e):
    title = '404 page not found'
    return render_template('404.html', title=title), 404


@app.errorhandler(500)
def internal_server_error(e):
    title = 'internal_server_error'
    return render_template('500.html', title=title), 500
