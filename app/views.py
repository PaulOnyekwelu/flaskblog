from app import app
from flask import render_template, url_for
from .process.forms import UserLoginForm, UserRegistrationForm

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
    user_login = UserLoginForm()
    return render_template('public/login.html', login = user_login, title = title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Registration Page'
    user_register  = UserRegistrationForm()
    return render_template('public/register.html', register = user_register, title = title)