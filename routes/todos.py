import json
from flask import jsonify, request, abort
from flask_restful import Resource
from flask_rest.models import Todo


class TodosAPI(Resource):
    def get(self):
        todos = Todo.get_all()
        results = []

        for todo in todos:
            obj = {
                'id': todo.id,
                'name': todo.name,
                'date_created': todo.date_created,
                'date_modified': todo.date_modified
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    def post(self):
        data = json.loads(request.data)
        name = data.get('name', '')

        if name:
            todo = Todo(name=name)
            todo.save()
            response = jsonify({
                'id': todo.id,
                'name': todo.name,
                'date_created': todo.date_created,
                'date_modified': todo.date_modified
            })
            response.status_code = 201
            return response


class TodoAPI(Resource):
    def get(self, id):
        todo = Todo.query.filter_by(id=id).first()
        if not todo:
            abort(404)  # Raise an HTTPException with a 404 not found status code

        response = jsonify({
            'id': todo.id,
            'name': todo.name,
            'date_created': todo.date_created,
            'date_modified': todo.date_modified
        })
        response.status_code = 200
        return response

    def put(self, id):
        todo = Todo.query.filter_by(id=id).first()
        if not todo:
            abort(404)  # Raise an HTTPException with a 404 not found status code

        data = json.loads(request.data)
        name = data.get('name', '')

        todo.name = name
        todo.save()
        response = jsonify({
            'id': todo.id,
            'name': todo.name,
            'date_created': todo.date_created,
            'date_modified': todo.date_modified
        })
        response.status_code = 200
        return response

    def delete(self, id):
        todo = Todo.query.filter_by(id=id).first()
        if not todo:
            abort(404)  # Raise an HTTPException with a 404 not found status code

        todo.delete()
        return {
            "message": "todo {} deleted successfully".format(todo.id)
        }, 200
