import os
from app import app, db
from flask import render_template, url_for, redirect, request, flash
from flask import send_from_directory
from app.model import db, Post, Admin, Category, Comment
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
@app.route('/admin/new-post/<id>', methods=["GET", "POST"])
@login_required
def newPost(id=''):
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
            edit_id = rec['id']
            query = Post.query.get(edit_id)
            query.post_author = author
            query.post_title = title
            query.post_content = content
            query.post_cat = cat
            query.post_date = date
            message = "Post was successfully updated"
        else:
            # this processes the add post function
            post = Post(author, title, content, date, cat)
            db.session.add(post)
            
            message = "New Post was added successfully"
        db.session.commit()
        flash(message)
        return redirect(url_for("viewPost"))
    elif request.method == 'GET':
        edit = Post.query.get(id)
        # author.data = edit.post_author

    return render_template('admin/new_post.html', title=title,
                           admins=admin_data, categories=categories_data,
                           edit=edit)


@app.route('/admin/viewpost')
@login_required
def viewPost():
    title = 'Admin Post'
    # querying the database for post information
    data = Post.query.order_by(Post.post_id.desc())
    return render_template('admin/view_post.html', title=title, posts=data)


@app.route('/admin/viewpost-<del_id>')
def post_del(del_id):
    # for deleting post based on their id in the database
    post = Post.query.get(del_id)
    Comment.query.filter_by(post_id=del_id).delete()
    db.session.delete(post)
    db.session.commit()
    flash('Category deleted successfully', "danger")
    return redirect(url_for("viewPost"))


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
