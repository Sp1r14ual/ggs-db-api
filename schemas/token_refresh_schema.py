from marshmallow import Schema, fields


class TokenRefreshSchema(Schema):
    access_token = fields.Str(dump_only=True)
