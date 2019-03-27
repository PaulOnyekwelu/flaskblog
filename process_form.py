from wtforms import Form, StringField, PasswordField, SubmitField

class UserLoginForm(Form):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('sign up')
