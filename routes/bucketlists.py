import json
from flask import jsonify, request, abort
from flask_restful import Resource
from flask_rest.models import Bucketlist


class BucketlistsAPI(Resource):
    def get(self):
        bucketlists = Bucketlist.get_all()
        results = []

        for bucketlist in bucketlists:
            obj = {
                'id': bucketlist.id,
                'name': bucketlist.name,
                'date_created': bucketlist.date_created,
                'date_modified': bucketlist.date_modified
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    def post(self):
        data = json.loads(request.data)
        name = data.get('name', '')

        if name:
            bucketlist = Bucketlist(name=name)
            bucketlist.save()
            response = jsonify({
                'id': bucketlist.id,
                'name': bucketlist.name,
                'date_created': bucketlist.date_created,
                'date_modified': bucketlist.date_modified
            })
            response.status_code = 201
            return response


class BucketlistAPI(Resource):
    def get(self, id):
        bucketlist = Bucketlist.query.filter_by(id=id).first()
        if not bucketlist:
            abort(404)  # Raise an HTTPException with a 404 not found status code

        response = jsonify({
            'id': bucketlist.id,
            'name': bucketlist.name,
            'date_created': bucketlist.date_created,
            'date_modified': bucketlist.date_modified
        })
        response.status_code = 200
        return response

    def put(self, id):
        bucketlist = Bucketlist.query.filter_by(id=id).first()
        if not bucketlist:
            abort(404)  # Raise an HTTPException with a 404 not found status code

        data = json.loads(request.data)
        name = data.get('name', '')

        bucketlist.name = name
        bucketlist.save()
        response = jsonify({
            'id': bucketlist.id,
            'name': bucketlist.name,
            'date_created': bucketlist.date_created,
            'date_modified': bucketlist.date_modified
        })
        response.status_code = 200
        return response

    def delete(self, id):
        bucketlist = Bucketlist.query.filter_by(id=id).first()
        if not bucketlist:
            abort(404)  # Raise an HTTPException with a 404 not found status code

        bucketlist.delete()
        return {
            "message": "bucketlist {} deleted successfully".format(bucketlist.id)
        }, 200
