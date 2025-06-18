from flask_restful import Api,Resource
from models import Course
from flask import request
from app import app


api =Api(app)



# begin of courses routes
class Courses(Resource):
    def get(self):
        courses =Course.query.all()
        return [course.to_dict() for course in courses],200

    def post(self):
        pass

class CoursesByID(Resource):
    def get(self,id):
        course = Course.query.filter_by(id=id).first()
        return course.to_dict(),200
    def patch(self,id):
        pass
    def delete(self,id):
        pass