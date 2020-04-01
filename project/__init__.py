import os
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# Instantiate App using reserved name variable from python cli
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# Instantiate db
db = SQLAlchemy(app)

# Create User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False) 
    active = db.Column(db.Boolean, default=True, nullable=False) 
    
    def __init__(self):
        self.username = username
        self.email = email

class Ping(Resource):
    def get(self):
        return {
                'message': 'pong!',
                'status': 'success'
                }


app.config.from_object('project.config.DevelopmentConfig')

api.add_resource(Ping, '/ping')

