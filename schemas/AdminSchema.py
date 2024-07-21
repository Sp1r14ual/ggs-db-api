from marshmallow import Schema, fields


class AdminSchema(Schema):
    login = fields.Str(required=True, load_only=True)
