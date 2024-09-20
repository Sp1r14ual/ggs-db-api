from marshmallow import Schema, fields


class GetAllHousesSchema(Schema):
    id_client = fields.Int(required=False, load_only=True)
    id_organization = fields.Int(required=False, load_only=True)
