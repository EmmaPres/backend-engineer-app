from marshmallow import Schema, fields


class EmployeeSchema(Schema):
    id = fields.Int()
    gender = fields.String(required=True)