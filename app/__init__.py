from flask import Flask
#App config
app = Flask(__name__)
app.secret_key ='hello from silanka'

site_name ="silanka blog"

from app.pyfiles import views
from app.pyfiles import admin_views