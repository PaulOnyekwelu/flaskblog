from app import app
from flask import render_template, url_for, redirect, request, flash
from wtforms import Form, StringField, PasswordField, validators


class UserRegistration(Form):
    fname = StringField('First Name',
                        [validators.DataRequired(),
                            validators.Length(min=3, max=30)])
    lname = StringField('Last Name',
                        [validators.DataRequired(),
                            validators.Length(min=3, max=30)])
    email = StringField('Email',
                        [validators.email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), 
                                          validators.EqualTo('confirm', 
                                          message='both password must match')])
    confirm = PasswordField('Confirm Password',
                            [validators.DataRequired()])


@app.route('/admin/hide/register', methods=['GET', 'POST'])
def register():
    title = 'Registration Page'
    form = UserRegistration()
    if request.method == 'POST':
        flash('Registration Successful')
    return render_template('admin/hide/register.html', title=title, form=form)
