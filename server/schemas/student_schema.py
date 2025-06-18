from server.models import Student,db
from marshmallow import Schema, fields, validate, validates, ValidationError

class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    age = fields.Int(required=True, validate=validate.Range(min=1))

    # You can nest enrollments later if needed
