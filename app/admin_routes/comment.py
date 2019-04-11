from app import app
from flask import render_template, url_for, redirect, request, flash
from flask_login import current_user


@app.route('/admin/comment')
def comment():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    elif current_user.is_authenticated:
        title = 'Admin Comment'
        return render_template('admin/comment.html', title=title)
