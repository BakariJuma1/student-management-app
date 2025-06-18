from server.models.db import db
from sqlalchemy.orm import relationship

class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    enrollments = db.relationship("Enrollment", back_populates="course")
   