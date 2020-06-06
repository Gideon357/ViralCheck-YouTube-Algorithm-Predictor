from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bd945ab5ed262199283e9bf2fa55c269'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)

  def __repr__(self):
    value = 'User({}, {}, {})'.format(self.username, self.email, self.image_file)
    return value


class Post(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    value = 'Post({}, {})'.format(self.title, self.date_posted)
    return value


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
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account succesfully created for {form.username.data}!', 'success')
    return redirect(url_for("home"))
  return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('You have been logged in!', 'success')
      return redirect(url_for("home"))
    else:
      flash('Login Unsuccessful, please check username and password', 'danger')

  return render_template("login.html", form=form)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)