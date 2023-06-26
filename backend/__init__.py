from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
databaseName = 'pythonsqlite.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:////{os.path.join(os.getcwd(),'backend','database',databaseName)}"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:////{os.path.join('/home/DrKakku/Question-Tracker-app','backend','database',databaseName)}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
print(app.config['SQLALCHEMY_DATABASE_URI'])

# connectDb("./backend/database/pythonsqlite.db")

from backend import routes

cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

