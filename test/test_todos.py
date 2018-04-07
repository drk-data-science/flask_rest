import pytest
import flask
from flask import Flask
from flask_restful import Api
import json
from flask_sqlalchemy import SQLAlchemy
from bucketlist.app import app, db


class TestApp:
    """This class represents the todo test case"""

    def setup(self):
        """Define test variables and initialize app."""
        with app.app_context():
            db.create_all()

        self.client = app.test_client()
        self.todo = {'name': 'Buy milk for kids'}

    def test_todo_creation(self):
        """Test API can create a todo (POST request)"""
        with app.test_request_context():
            res = self.client.post(
                '/todos/',
                data=json.dumps(self.todo))
            assert res.status_code == 201
            assert 'Buy milk' in res.data.decode('utf-8')

    def test_api_can_get_all_todos(self):
        """Test API can get a todo (GET request)."""
        with app.test_request_context():
            res = self.client.post(
                '/todos/',
                data=json.dumps(self.todo))
            assert res.status_code == 201

            res = self.client.get(
                '/todos/')
            assert res.status_code == 200
            assert 'Buy milk' in res.data.decode('utf-8')

    def test_api_can_get_todo_by_id(self):
        """Test API can get a single todo by using it's id."""
        with app.test_request_context():
            rv = self.client.post(
                '/todos/',
                data=json.dumps(self.todo))
            assert rv.status_code == 201

            result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
            result = self.client.get(
                '/todos/{}'.format(result_in_json['id']))
            assert result.status_code == 200
            assert 'Buy milk' in str(result.data)

    def test_todo_can_be_edited(self):
        """Test API can edit an existing todo. (PUT request)"""
        with app.test_request_context():
            rv = self.client.post(
                '/todos/',
                data=json.dumps({'name': 'Eat, pray and love'}))
            assert rv.status_code == 201

            rv = self.client.put(
                '/todos/1',
                data=json.dumps({"name": "Dont just eat, but also pray and love :-)"}))
            assert rv.status_code == 200
            results = self.client.get('/todos/1')
            assert 'Dont just eat' in rv.data.decode('utf-8')

    def test_todo_deletion(self):
        """Test API can delete an existing todo. (DELETE request)."""
        with app.test_request_context():
            rv = self.client.post(
                '/todos/',
                data=json.dumps({'name': 'Eat, pray and love'}))
            assert rv.status_code == 201

            res = self.client.delete('/todos/1')
            assert res.status_code == 200

        # Test to see if it exists, should return a 404
        result = self.client.get('/todos/1')
        assert result.status_code == 404

    def teardown(self):
        """teardown all initialized variables."""
        with app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()
