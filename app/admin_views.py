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

@app.route('/admin/register', methods=['GET', 'POST'])
def register():
    title = 'Registration Page'
    return render_template('admin/hide/register.html', title = title)

@app.route('/admin/new-post')
def newPost():
    return render_template('admin/new_post.html')

@app.route('/admin/view-post')
def viewPost():
    return render_template('admin/view_post.html')

@app.route('/admin/category')
def category():
    return render_template('admin/category.html')

@app.route('/admin/comment')
def comment():
    return render_template('admin/comment.html')

@app.route('/admin/settings')
def siteSetting():
    return render_template('admin/site_setting.html')


