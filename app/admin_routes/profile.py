from app import app
from flask import render_template, url_for, redirect, request, flash
from flask_login import current_user


@app.route('/admin/profile')
def profile():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    elif current_user.is_authenticated:
        title = 'Admin Profile'
        return render_template('admin/profile.html', title=title)
