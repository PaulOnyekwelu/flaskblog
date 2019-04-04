from flask import Flask, render_template
#App config
app = Flask(__name__)
app.secret_key ='hello from silanka'

site_name ="silanka blog"

from app.pyfiles import views
from app.pyfiles import admin_views

@app.errorhandler(404)
def page_not_found(e):
    title='404 page not found'
    return render_template('404.html', title=title), 404

@app.errorhandler(500)
def internal_server_error(e):
    title='internal_server_error'
    return render_template('500.html', title=title), 500