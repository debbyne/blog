from unicodedata import category
from flask import render_template,redirect,url_for,abort

from app.main.forms import CommentForm, NewBlogForm,UpdateProfile
from . import main
from flask_login import current_user, login_required
from .. import  photos, db
from sqlalchemy import desc
from ..models import Comment, User,Post,Quote
from ..requests import get_quote

@main.route('/')
def index():
    quote = get_quote()
    posts = Post.query.all()
    title = ' Blogs'

    post = Post.query.filter_by(id = Post.id).first()
    # user = User.query.filter_by(username = current_user).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment= comment ,post = post,user=current_user)
        new_comment.save_comment()
    return render_template('index.html', title = title,quote = quote, posts = posts,CommentForm = form)

@main.route('/new/blog/', methods = ['GET','POST'])
@login_required
def newblog():
    form = NewBlogForm()
    if form.validate_on_submit():
        new_post = Post(title = form.title.data, content = form.post.data, user=current_user)
        new_post.save_post()
        post = Post.query.filter_by(title=new_post.title).first()
        return redirect(url_for('main.index'))
    
    return render_template('newblog.html',form = form) 

@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/blog/', methods = ['GET' ,'POST'])
def blog():
    quote = Quote.query.all()
    post = Post.query.filter_by(id = Post.id).first()
    user = User.query.filter_by(username = current_user).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment= comment,post = post,user = current_user )
        new_comment.save_comment()

    return render_template('blog.html' , post = post , CommentForm = form)
