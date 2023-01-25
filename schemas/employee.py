from marshmallow import Schema, fields


# Defines how to serialize/deserialize an Employee, in the employees db.
class EmployeeSchema(Schema):
    id = fields.Int()
    gender = fields.String(required=True)