from app import app
from flask import render_template, url_for, redirect, request, flash
from app.pyfiles.dbase import mysql

@app.route('/admin/register', methods=['GET', 'POST'])
def register():
    title = 'Registration Page'
    return render_template('admin/hide/register.html', title = title)