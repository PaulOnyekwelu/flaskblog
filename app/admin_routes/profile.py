from app import app
from flask import render_template, url_for, redirect, request, flash


@app.route('/admin/profile')
def profile():
    title = 'Admin Profile'
    return render_template('admin/profile.html', title=title)