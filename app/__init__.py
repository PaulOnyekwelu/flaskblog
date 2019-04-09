from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# App config
app = Flask(__name__)

app.secret_key = 'gdfght6y79uhg54'
path = "mysql://root:root@localhost/flask_blog"
app.config['SQLALCHEMY_DATABASE_URI'] = path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
