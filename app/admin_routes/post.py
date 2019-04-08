from app import app
from flask import render_template, url_for, redirect, request, flash
from app.config import db, Post, Admin, Category
from datetime import datetime


@app.route('/admin/new-post', methods=["GET", "POST"])
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
        content = rec['post_content']
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
def viewPost():
    title = 'Admin Post'
    return render_template('admin/view_post.html', title=title)                                           