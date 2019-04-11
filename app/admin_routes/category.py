from app import app, db
from flask import render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from app.model import Category
from datetime import datetime
from flask_login import current_user


@app.route('/admin/category', methods=['GET', 'POST'])
def category():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    elif current_user.is_authenticated:
        title = 'Admin Category'
        if request.method == 'POST':
            cat = request.form
            cat_name = cat['cat_name']
            cat_url = cat['cat_url']
            cat_date = datetime.now()

            if cat['cat_id'] != '':
                # this process edits a selected category
                data_id = cat['cat_id']
                cat = Category.query.filter_by(cat_id=data_id).one()
                cat.cat_name = cat_name
                cat.cat_url = cat_url
                cat.date_added = cat_date
                message = 'Category was updated successfully'
            else:
                # this process adds new category
                cat = Category(cat_name, cat_url, cat_date)
                db.session.add(cat)
                message = 'Category was added successfully'
            db.session.commit()
            flash(message, "success")
            return redirect(request.url)

        # this process retrieves data from database and displays it to the user
        data = Category.query.all()
        return render_template('admin/category.html',
                               categories=data, title=title)


@app.route('/delete/<string:del_id>')
def delete(del_id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    elif current_user.is_authenticated:
        # this deletes a category
        data = Category.query.get(del_id)
        db.session.delete(data)
        db.session.commit()
        flash('Category deleted successfully', "danger")
        return redirect(url_for('category'))
