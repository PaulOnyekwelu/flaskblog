from app import app
from flask import render_template, url_for, redirect, request, flash


@app.route('/admin/category', methods=['GET', 'POST'])
def category():
    title = 'Admin Category'
    if request.method == 'POST':
        cat = request.form
        cat_name = cat['cat_name']
        cat_url = cat['cat_url']
        cat_date = cat['date_added']
        cur = mysql.connection.cursor()

        if cat['cat_id'] != '':
            # this process edits a selected category
            data_id = cat['cat_id']
            cur.execute("""
                UPDATE category SET cat_name=%s, cat_url=%s, date_added=%s
                WHERE cat_id=%s
            """, (cat_name, cat_url, cat_date, data_id))
            message = 'Category was updated successfully'
        else:
            # this process adds new category
            cur.execute('''
                                INSERT INTO
                                category(cat_name, cat_url, date_added)
                                VALUES(%s, %s, %s)
                                ''', (cat_name, cat_url, cat_date))
            message = 'Category was added successfully'
        mysql.connection.commit()
        flash(message)
        return redirect(request.url)

    # this process retrieves data from database and displays it to the user
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM category")
    data = cur.fetchall()
    cur.close()

    return render_template('admin/category.html', categories=data, title=title)


@app.route('/delete/<string:del_id>')
def delete(del_id):
    # this deletes a category
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM category WHERE cat_id = %s", (del_id,))
    mysql.connection.commit()
    flash('Category deleted successfully')
    return redirect(url_for('category'))
