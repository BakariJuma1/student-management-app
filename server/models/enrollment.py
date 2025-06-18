from server.models.db import db
from sqlalchemy import  ForeignKey



class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.Integer(), ForeignKey("students.id", ondelete="CASCADE"))
    course_id = db.Column(db.Integer(), ForeignKey("courses.id", ondelete="CASCADE"))

    student = db.relationship("Student", back_populates="enrollments")
    course = db.relationship("Course", back_populates="enrollments")
 