from .db import db
from sqlalchemy_serializer import SerializerMixin

class Student(db.Model,SerializerMixin):
    
    __tablename__ = "students"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer())

    enrollments = db.relationship(
        "Enrollment", 
        back_populates="student" ,
        cascade='all')
    
    serialize_rules = ("-enrollments.student",)
    