from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app=Flask(__name__)

app.config['SECRET_KEY'] ='03ab733539228fc6a292092770c88c4a'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db= SQLAlchemy(app)
bcrypt = Bcrypt(app)

from pitch import routes
