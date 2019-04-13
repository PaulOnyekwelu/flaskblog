import os
from app import app, db
from flask import render_template, url_for, redirect, request, flash
from flask import send_from_directory
from app.model import db, Post, Admin, Category
from datetime import datetime
from flask_ckeditor import CKEditor, upload_fail, upload_success
from flask_wtf import CSRFProtect
from flask_login import login_required

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
app.config['CKEDITOR_ENABLE_CSRF'] = True
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')

ckeditor = CKEditor(app)
csrf = CSRFProtect(app)


@app.route('/admin/new-post', methods=["GET", "POST"])
@login_required
def newPost():
    title = 'Admin New Post'
    # this pulls information from the admin and category table made
    # available in the respective section in the add post form
    admin_data = Admin.query.all()
    categories_data = Category.query.all()
    # creating the add and add post process
    if request.method == "POST":
        rec = request.form
        author = rec['post_author']
        title = rec['post_title']
        content = rec['ckeditor']
        cat = rec['post_cat']
        date = datetime.now()
        if rec['id']:
            # this processes the edit post function
            pass
        else:
            # this processes the add post function
            post = Post(author, title, content, date, cat)
            db.session.add(post)
            db.session.commit()
            message = "New Post was added successfully"
        flash(message)
        return redirect(url_for("viewPost"))
    return render_template('admin/new_post.html', title=title,
                           admins=admin_data, categories=categories_data)


@app.route('/admin/view-post')
@login_required
def viewPost():
    title = 'Admin Post'
    # querying the database for post information
    data = Post.query.all()
    return render_template('admin/view_post.html', title=title, posts=data)


@app.route('/files/<filename>')
@login_required
def uploaded_files(filename):
    path = app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)


@app.route('/upload', methods=['POST'])
@login_required
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url=url)
