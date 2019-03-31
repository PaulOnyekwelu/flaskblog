from app import app
from flask import render_template, url_for


app.config['SECRET_KEY'] = 'taoPSJfjPOjfkfsfD'
#front page routing
@app.route('/')
def home():
    title = 'Home Page'
    return render_template('public/index.html', title = title)

@app.route('/about')
def about():
    title = 'About'
    return render_template('public/about.html', title = title)

@app.route('/login', methods=['GET','POST'])
def login():
    title = 'Login Page'
    return render_template('public/login.html', title = title)
    
@app.route('/reset-password')
def forgot():
    title = 'Password Reset'
    return render_template('public/forgot.html', title = title)