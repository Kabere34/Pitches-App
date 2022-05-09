from flask import Flask,render_template, url_for
from forms import RegistrationForm,LoginForm

app=Flask(__name__)

app.config['SECRET_KEY'] ='03ab733539228fc6a292092770c88c4a'

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


@app.route("/register")
def register():
  form = RegistrationForm()
  return render_template('register.html',title='Register', form=form)

@app.route("/login")
def login():
  form = LoginForm()
  return render_template('login.html',title='Login', form=form)


if __name__ == "__main__":
  app.run(debug=True)
