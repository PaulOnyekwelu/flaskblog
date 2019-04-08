from app import app
from flask import render_template, url_for, redirect, request, flash
from wtforms import Form, StringField, PasswordField, validators
from app.config import Admin, db


# user registration form class
class UserRegistration(Form):
    fname = StringField('Full Name',
                        [validators.DataRequired(),
                            validators.Length(min=3, max=30)])
    username = StringField('Username',
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
    if request.method == 'POST' and form.validate:
        rec = request.form
        fullname = rec["fname"]
        username = rec["username"]
        email = rec["email"]
        password = rec["password"]
        if rec["id"] != "":
            pass
        else:
            user = Admin(fullname, username, email, password)
            db.session.add(user)
            db.session.commit()
            message = "User Successfully Registered!"
        flash(message)
        return redirect(url_for("dashboard"))

    return render_template('admin/hide/register.html', title=title, form=form)
