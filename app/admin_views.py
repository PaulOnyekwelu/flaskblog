from app import app
from flask import render_template, url_for

#admin page routing
@app.route('/admin/dashboard')
def dashboard():
    title = 'Admin Dashboard'

    return render_template('admin/dashboard.html', title = title)

@app.route('/admin/profile')
def profile():
    title = 'Admin Profile'
    return render_template('admin/profile.html', title = title)