from app import app
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required


@app.route('/admin/settings')
@login_required
def siteSetting():
    title = 'Admin Site Settings'
    return render_template('admin/site_setting.html', title=title)
