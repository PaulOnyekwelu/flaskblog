from app import app
from flask import render_template, url_for, redirect, request, flash
from flask_login import current_user


@app.route('/admin/dashboard')
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    elif current_user.is_authenticated:
        title = 'Admin Dashboard'
        return render_template('admin/dashboard.html', title=title)
