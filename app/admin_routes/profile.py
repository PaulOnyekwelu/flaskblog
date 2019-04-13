from app import app
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required


@app.route('/admin/profile')
@login_required
def profile():
    title = 'Admin Profile'
    return render_template('admin/profile.html', title=title)
