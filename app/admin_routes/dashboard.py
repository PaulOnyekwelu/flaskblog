from app import app
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required


@app.route('/admin/dashboard')
@login_required
def dashboard():
    title = 'Admin Dashboard'
    return render_template('admin/dashboard.html', title=title)
