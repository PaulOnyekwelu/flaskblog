from app import app
from flask import render_template, url_for
from .process.forms import UserLoginForm, UserRegistrationForm

app.config['SECRET_KEY'] = 'taoPSJfjPOjfkfsfD'
#front page routing
@app.route('/')
def home():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/login', methods=['GET','POST'])
def login():
    user_login = UserLoginForm()
    return render_template('public/login.html', login = user_login)

@app.route('/register', methods=['GET', 'POST'])
def register():
    user_register  = UserRegistrationForm()
    return render_template('public/register.html', register = user_register)