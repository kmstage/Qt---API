from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from FilterAPI.Config import *


app = Flask(__name__)
app.config['SECRET_KEY'] = app_secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
'''
--> use postgresql for deploy: 
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_username}:{db_password}@{db_server}/{db_name}?charset=utf8mb4'
'''
db = SQLAlchemy(app)

'''
from FilterAPI import routes must be at the end.
'''
from FilterAPI import routes
