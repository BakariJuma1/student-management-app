from flask_restful import Api,Resource
from models import Enrollment
from flask import request
from app import app


api =Api(app)

class Enrollments(Resource):
    def get(self):
        pass

class EnrollmentsByID(Resource):
    def get(self,id):
        pass
    def patch(self,id):
        pass
    def delete(self,id):
        pass   



api.add_resource(Enrollments, '/enrollments')
api.add_resource(EnrollmentsByID, '/enrollments/<int:id>')