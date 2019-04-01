from app import app
from flask import render_template, url_for, redirect, request, flash
from app.pyfiles.dbase import mysql

@app.route('/admin/settings')
def siteSetting():
    return render_template('admin/site_setting.html')