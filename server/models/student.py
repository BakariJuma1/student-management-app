from server.models.db import db
# from sqlalchemy.orm import relationship

class Student(db.Model):
    
    __tablename__ = "students"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer())

    enrollments = db.relationship(
        "Enrollment", 
        back_populates="student" ,
        cascade='all')
    