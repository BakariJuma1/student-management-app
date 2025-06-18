from flask_restful import Api,Resource
from server.models import Student
from flask import request
from server.models import db
from server.app import app
from server.schemas.student_schema import StudentSchema

api = Api(app)

class Students(Resource):
    def get(self):
        students= Student.query.all()
        student_schema = StudentSchema(many=True)

        if students:
            return student_schema.dump(students),200
        else:
            return {"message":"students not found"},404
    
    def post(self):
        data = request.get_json()
        try:
            validated_data = StudentSchema().load(data)
        except Exception as e:
            return {"message": str(e)}, 400
        
        new_student = Student(**validated_data)
        
        # Check if student already exists
        existing_student = Student.query.filter_by(name=new_student.name, age=new_student.age).first()
        if existing_student:
            return {"message": "Student already exists"}, 409
        
        # Add the new student to the database
        new_student.id = Student.query.count() + 1
        db.session.add(new_student)
        db.session.commit()
        return new_student.to_dict(),201

class StudentsByID(Resource):            
    def get(self,id):
        student = Student.query.filter_by(id=id).first()
        student_schema = StudentSchema()

        if student:
             return student_schema.dump(student),200  
        else:
            return {"message":"student not found"},404

      
    def patch(self,id):
        pass

    def delete(self,id):
        student = Student.query.filter_by(id=id).first()

        db.session.delete(student)
        db.session.commit()



api.add_resource(Students, '/students')
api.add_resource(StudentsByID, '/students/<int:id>')
