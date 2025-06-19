from .db import db
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

class Course(db.Model,SerializerMixin):
    __tablename__ = "courses"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    enrollments = db.relationship("Enrollment", back_populates="course")
    serialize_rules =('-enrollements.course')
   