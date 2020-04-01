from flask import Flask, jsonify
from flask_restx import Resource, Api

# Instantiate App using reserved name variable from python cli
app = Flask(__name__)

api = Api(app)


class Ping(Resource):
    def get(self):
        return {
                'status': 'success',
                'message': 'pong!'
                }


app.config.from_object('project.config.DevelopmentConfig')

api.add_resource(Ping, '/ping')

