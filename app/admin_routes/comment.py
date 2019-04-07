from app import app
from flask import render_template, url_for, redirect, request, flash


@app.route('/admin/comment')
def comment():
    title = 'Admin Comment'
    return render_template('admin/comment.html', title=title)