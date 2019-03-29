from flask import Flask
#App config
app = Flask(__name__)

site_name ="silanka blog"

from app import views
from app import admin_views