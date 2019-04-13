from app import app
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required


@app.route('/admin/comment')
@login_required
def comment():
    title = 'Admin Comment'
    return render_template('admin/comment.html', title=title)
