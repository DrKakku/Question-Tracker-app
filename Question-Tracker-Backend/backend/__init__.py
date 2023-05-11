from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/yashtripathi/Documents/OneDrive/yash docs/Work/CODE/Python/utilites/Question-Tracker-app/Question-Tracker-Backend/backend/database/pythonsqlite.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# connectDb("./backend/database/pythonsqlite.db")

from backend import routes
