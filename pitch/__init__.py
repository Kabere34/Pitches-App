from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SECRET_KEY'] ='03ab733539228fc6a292092770c88c4a'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db= SQLAlchemy(app)

from pitch import routes
