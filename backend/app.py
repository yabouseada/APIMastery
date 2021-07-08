from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from api.DbConnection import DbConnection
# from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DbConnection.connector()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = True

db = SQLAlchemy(app)

# User(db, db.Model)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

@app.route('/')
def get():
    return 'ok'