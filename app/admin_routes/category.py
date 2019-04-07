from app import app
from flask import render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from app.config import db, Category
from datetime import datetime


@app.route('/admin/cat', methods=['GET', 'POST'])
def category():
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
        flash(message)
        return redirect(request.url)

    # this process retrieves data from database and displays it to the user
    data = Category.query.all()
    return render_template('admin/category.html', categories=data, title=title)


@app.route('/delete/<string:del_id>')
def delete(del_id):
    # this deletes a category
    data = Category.query.filter_by(cat_id=del_id).first()
    db.session.delete(data)
    db.session.commit()
    flash('Category deleted successfully')
    return redirect(url_for('category'))
