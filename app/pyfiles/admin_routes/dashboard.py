from app import app
from flask import render_template, url_for, redirect, request, flash
from app.pyfiles.dbase import mysql

@app.route('/admin/dashboard')
def dashboard():
    title = 'Admin Dashboard'
    return render_template('admin/dashboard.html', title = title)