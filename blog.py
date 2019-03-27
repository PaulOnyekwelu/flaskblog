from flask import Flask, render_template, url_for
from process_form import UserLoginForm

#App config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'taoPSJfjPOjfkfsfD'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = UserLoginForm()
    return render_template('login.html', form = form)

@app.route('/register')
def register():
    return render_template('register.html')






if __name__ == '__main__':
    app.run(debug=True)
