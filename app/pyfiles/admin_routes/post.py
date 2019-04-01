from app import app
from flask import render_template, url_for, redirect, request, flash
from app.pyfiles.dbase import mysql

@app.route('/admin/new-post')
def newPost():
    return render_template('admin/new_post.html')

@app.route('/admin/view-post')
def viewPost():
    return render_template('admin/view_post.html')