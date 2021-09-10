from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Patientdata.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
 

db = SQLAlchemy(app)

from applications import routes