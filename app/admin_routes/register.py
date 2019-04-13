from app import app, db, bcrypt
from flask import render_template, url_for, redirect, request, flash
from wtforms import Form, StringField, PasswordField, validators
from app.model import Admin
from flask_login import login_required


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
    password = PasswordField('Password', [validators.DataRequired()])
    confirm = PasswordField('Confirm Password',
                            validators=[validators.DataRequired(),
                                        validators.EqualTo('password')])

    def validate_username(self, username):
        user = Admin.query.filter_by(admin_username=username.data).first()
        if user:
            raise validators.ValidationError("""
            username not available, choose a different one""")

    def validate_email(self, email):
        user = Admin.query.filter_by(admin_email=email.data).first()
        if user:
            raise validators.ValidationError('''
            email already in use by another account''')


@app.route('/admin/hide/register', methods=['GET', 'POST'])
@login_required
def register():
    title = 'Registration Page'
    form = UserRegistration(request.form)
    if request.method == 'POST' and form.validate():
        rec = request.form
        fullname = form.fname.data
        username = form.username.data
        email = form.email.data
        pwd = bcrypt.generate_password_hash(form.password.data)
        password = pwd.decode("utf-8")
        if rec["id"] != "":
            pass
        else:
            user = Admin(fullname, username, email, password)
            db.session.add(user)
            db.session.commit()
            message = "User Successfully Registered!"
        flash(message)
        return redirect(url_for("dashboard"))

    return render_template('admin/hide/register.html',
                           title=title, form=form)
