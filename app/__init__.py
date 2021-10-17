from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import environ 
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI') #Postgresql connection
app.config["SQLALCHEMY_BINDS"] = {
'db1': environ.get('SQLALCHEMY_DATABASE_URI'),
'db2': environ.get('SQLALCHEMY_DATABASE_URL')
}

db = SQLAlchemy(app)



from app import routes