from app import app, db
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required
from app.model import Comment


@app.route('/admin/comment')
@login_required
def comment():
    title = 'Admin Comment'
    comment = Comment.query.all()
    return render_template('admin/comment.html', title=title, comments=comment)


@app.route('/admin/comment/del-<del_id>')
@login_required
def del_comment(del_id):
    # this deletes a category
    data = Comment.query.get(del_id)
    db.session.delete(data)
    db.session.commit()
    flash('Category deleted successfully', "danger")
    return redirect(url_for('comment'))
