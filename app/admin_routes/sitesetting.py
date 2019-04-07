from app import app
from flask import render_template, url_for, redirect, request, flash


@app.route('/admin/settings')
def siteSetting():
    title = 'Admin Site Settings'
    return render_template('admin/site_setting.html', title=title)