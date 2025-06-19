from .db import db
from sqlalchemy_serializer import SerializerMixin


class Gender(db.Model,SerializerMixin):
    __tablename__ = "gender"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
 