from app import app
from flask import render_template, url_for, redirect, request, flash
from app.pyfiles.dbase import mysql

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

@app.route('/admin/category', methods = ['GET', 'POST'])
def category():
    #this process the category form for adding new category
    if request.method == 'POST':
        
        cat = request.form
        cat_name = cat['cat_name']
        cat_url = cat['cat_url']
        cat_date = cat['date_added']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO category(cat_name, cat_url, date_added) VALUES(%s, %s, %s)',
                            (cat_name, cat_url, cat_date))
        mysql.connection.commit()
        flash('Category added Successfully!')
        return redirect(url_for('category'))
    
    #this process retrieves data from database and displays it to the user
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM category")
    data = cur.fetchall()
    cur.close()

    return render_template('admin/category.html', categories = data)

@app.route('/admin/comment')
def comment():
    return render_template('admin/comment.html')

@app.route('/admin/settings')
def siteSetting():
    return render_template('admin/site_setting.html')