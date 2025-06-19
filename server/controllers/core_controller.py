from flask_restful import Resource
from server.models import Student
from flask import request
from models import db




# refactoring it into a reusable codebase

class CoreController(Resource):

    def __init__(self,model):
        super().__init__()
        self.Model = model

    def get(self):
        all= self.Model.query.all()

        if all:
            return all.to_dict(),200
        else:
            return {"message":"students not found"},404
    
    def post(self):
        data = request.get_json()
        try:
            new_resource = Student(**data)
            existing_student = Student.query.filter_by(name=new_resource.name,age=new_resource.age).first()
            if existing_student:
                return {"message":"student already exist"},409
            db.session.add(new_resource)
            db.session.commit()
        except Exception as e:
            return {"message": str(e)}, 400

class CoreControllerOne(Resource): 

    def __init__(self,model):
        super().__init__()
        self.Model = model  

    def get(self,id):
        one_by_id = self.Model.query.filter_by(id=id).first()
       

        if one_by_id:
             return one_by_id.to_dict(),200  
        else:
            return {"message":"student not found"},404

      
    def patch(self,id):
        one = self.Model.query.filter_by(id=id).first()
        if not one:
            return {"message":"Student not found"},404
        data = request.get_json()
        for key,value in data.items():
            setattr(one,key,value)
        db.session.commit()
        return one.to_dict(),200    



    def delete(self,id):
        one = self.Model.query.filter_by(id=id).first()
        if not one:
            return {"message":"Student not found"}

        db.session.delete(one)
        db.session.commit()
        return {"message":"Student deleted"}

