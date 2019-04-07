from app import app
from flask import render_template, url_for, redirect, request, flash
from app.config import db, Category
from datetime import datetime


@app.route('/admin/new-post', methods=["GET", "POST"])
def newPost():
    title = 'Admin New Post'

    return render_template('admin/new_post.html', title=title)


@app.route('/admin/view-post')
def viewPost():
    title = 'Admin Post'
    return render_template('admin/view_post.html', title=title)                                           