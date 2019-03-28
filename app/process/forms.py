from wtforms import Form, StringField, PasswordField, SubmitField, validators


class UserLoginForm(Form):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('Sign In')

class UserRegistrationForm(Form):
    first = StringField('firstname')
    last = StringField('lastname')
    username = StringField('username')
    password = PasswordField('password', [validators.EqualTo('confirm')])
    confirm = PasswordField('confirm')
    submit = SubmitField('Sign Up')