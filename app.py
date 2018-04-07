import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from bucketlist.config import app_config

# modified from
# https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way
# http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
# https://tutorials.technology/tutorials/59-Start-a-flask-project-from-zero-building-api-rest.html


config_name = os.getenv('APP_SETTINGS')  # config_name = "development"
# app = Flask(__name__, instance_relative_config=True)
app = Flask(__name__)
app.config.from_object(app_config[config_name])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

from bucketlist.models import Bucketlist
from bucketlist.models import Todo
from bucketlist.routes.bucketlists import BucketlistsAPI, BucketlistAPI
from bucketlist.routes.todos import TodosAPI, TodoAPI

with app.app_context():
    db.create_all()

api.add_resource(BucketlistsAPI, '/bucketlists/', endpoint='bucketlists')
api.add_resource(BucketlistAPI, '/bucketlists/<int:id>', endpoint='bucketlist')

api.add_resource(TodosAPI, '/todos/', endpoint='todos')
api.add_resource(TodoAPI, '/todos/<int:id>', endpoint='todo')
