from flask import Flask
#App config
app = Flask(__name__)

from app import views
from app import admin_views