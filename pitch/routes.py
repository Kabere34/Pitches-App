from flask import render_template, url_for, flash,redirect
from pitch import app, db, bcrypt
from pitch.forms import RegistrationForm,LoginForm
from pitch.models import User, Post

posts=[
  {
    'author': 'John',
    'title':'blog post',
    'content':'First post',
    'date_posted':'April 14, 2014',
  },
  {
    'author': 'Jane',
    'title':'video post',
    'content':'Second post',
    'date_posted':'July 14, 2015',
  }
]

@app.route("/")
def home():
    return render_template('index.html',posts=posts)

@app.route("/pickup")
def about():
    return render_template('pickup.html')


@app.route("/register", methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data,password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in', 'success')
    return redirect(url_for('login'))

  return render_template('register.html',title='Register', form=form)

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data=='admin@blog.com' and form.password.data=='password':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login unseccessful. Please check your username and password','danger')

  return render_template('login.html',title='Login', form=form)
