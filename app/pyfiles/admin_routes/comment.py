from app import app
from flask import render_template, url_for, redirect, request, flash
from app.pyfiles.dbase import mysql

@app.route('/admin/comment')
def comment():
    return render_template('admin/comment.html')