from flask import render_template, url_for, flash,redirect
from pitch import app, db, bcrypt
from pitch.forms import RegistrationForm,LoginForm
from pitch.models import User, Post
from flask_login import login_user, current_user, logout_user

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
  if current_user.is_authenticated:
    return redirect(url_for('home'))
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
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      return redirect(url_for('home'))
    else:
      flash('Login unseccessful. Please check your email and password','danger')

  return render_template('login.html',title='Login', form=form)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('home'))
