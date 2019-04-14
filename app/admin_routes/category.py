from app import app, db
from flask import render_template, url_for, redirect, request, flash
from app.model import Category
from datetime import datetime
from flask_login import login_required


@app.route('/admin/category', methods=['GET', 'POST'])
@login_required
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
        flash(message, "success")
        return redirect(request.url)

    # this process retrieves data from database and displays it to the user
    data = Category.query.all()
    return render_template('admin/category.html',
                           categories=data, title=title)


@app.route('/admin/category/<string:del_id>')
@login_required
def del_category(del_id):
    # this deletes a category
    data = Category.query.get(del_id)
    db.session.delete(data)
    db.session.commit()
    flash('Category deleted successfully', "danger")
    return redirect(url_for('category'))
