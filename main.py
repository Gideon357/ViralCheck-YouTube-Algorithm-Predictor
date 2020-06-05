from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

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
  return render_template('index.html')

@app.route('/advice')
def advice():
  return render_template("advice.html")

@app.route('/images')
def images():
  return render_template("instagram.html", posts=posts)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)