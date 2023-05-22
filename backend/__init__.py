from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
databaseName = 'pythonsqlite.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:////{os.path.join(os.getcwd(),'backend','database',databaseName)}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# connectDb("./backend/database/pythonsqlite.db")

from backend import routes
