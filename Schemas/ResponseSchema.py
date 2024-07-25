from marshmallow import Schema, fields


class AddSchema(Schema):
    id = fields.Int(dump_only=True)
    status_code = fields.Int(dump_only=True)


class EditDeleteSchema(Schema):
    status_code = fields.Int(dump_only=True)
