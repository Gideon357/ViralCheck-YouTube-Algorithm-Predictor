from flask import render_template, request, redirect, url_for, flash
from main import app, db, bcrypt
from main.forms import RegistrationForm, LoginForm
from main.models import User, Post
from model import likes, views, thumbnail
from flask_login import login_user, current_user, logout_user, login_required

posts = [
  {
    'author': 'Ali',
    'title': 'Post 1',
    'content': 'First post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1494253109108-2e30c049369b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80'
  },
  {
    'author': 'Bob',
    'title': 'Post 2',
    'content': 'Second post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1494253109108-2e30c049369b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80'
  },
  {
    'author': 'Bob',
    'title': 'Post 2',
    'content': 'Second post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1494253109108-2e30c049369b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80'
  },
  {
    'author': 'Bob',
    'title': 'Post 2',
    'content': 'Second post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1494253109108-2e30c049369b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80'
  },
  {
    'author': 'Bob',
    'title': 'Post 2',
    'content': 'Second post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1494253109108-2e30c049369b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80'
  },
  {
    'author': 'Bob',
    'title': 'Post 2',
    'content': 'Second post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1494253109108-2e30c049369b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80'
  }
]

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/advice')
def advice():
  return render_template("advice.html")

@app.route('/images')
def images():
  return render_template("instagram.html", posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Account created. You can now log in!', 'success')
    return redirect(url_for("login"))
  return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('home'))
    else:
      flash('Login Unsuccessful, please check email and password', 'danger')

  return render_template("login.html", form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
  return render_template("account.html")

@app.route('/user')
def user():
	return request.args['url']