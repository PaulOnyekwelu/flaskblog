from app import app, bcrypt, login_manager
from flask import render_template, url_for, request, redirect, flash
from app.model import Category, Post, Admin
from flask_login import login_user, current_user, logout_user


# front page routing
@app.route('/')
def home():
    title = 'Home Page'
    cat = Category.query.all()
    post = Post.query.all()

    return render_template('public/index.html', title=title,
                           category=cat, posts=post)


@app.route('/about')
def about():
    title = 'About'
    return render_template('public/about.html', title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    title = 'Login Page'
    if request.method == "POST":
        user = Admin.query.filter_by(admin_email=request.form["email"]).first()
        if user and bcrypt.check_password_hash(user.password,
                                               request.form["password"]):
            login_user(user, remember=request.form.get('remember'))
            flash("you are successfully logged in!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("invalid Login Details", "danger")
    return render_template('public/login.html', title=title)

# validation of remember token
@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


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
