from marshmallow import Schema, fields


class AdminSchema(Schema):
    login = fields.Str(required=True, load_only=True)
    access_token = fields.Str(dump_only=True)
    refresh_token = fields.Str(dump_only=True)
