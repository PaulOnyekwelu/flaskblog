from app import app, db, bcrypt, login_manager
from flask import render_template, url_for, request, redirect, flash
from app.model import Category, Post, Admin, Comment
from flask_login import login_user, current_user, logout_user, login_required


# front page routing
@app.route('/')
@app.route('/<int:page_num>')
def home():
    title = 'Home Page'
    cat = Category.query.all()
    post = Post.query.paginate(per_page=2, error_out=True)

    return render_template('public/index.html', title=title,
                           category=cat, posts=post)


@app.route('/post-<int:post_id>', methods=["GET", "POST"])
def post(post_id):
    title = 'Post'
    # processing comments by users and guest
    if request.method == "POST":
        rec = request.form
        name = rec["name"]
        email = rec["email"]
        content = rec["content"]
        post_id = rec["post_id"]

        # processing the add comment to post
        comment = Comment(name, email, content, post_id)
        db.session.add(comment)
        db.session.commit()
        return redirect(request.url)

    post = Post.query.filter_by(post_id=post_id).first()
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template('public/post.html', title=title, post=post,
                           comments=comments)


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
            next_page = request.args.get("next")
            dashboard = url_for('dashboard')
            flash("you are successfully logged in!", "success")
            return redirect(next_page) if next_page else redirect(dashboard)
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
