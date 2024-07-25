from marshmallow import Schema, fields


class AddHouseSchema(Schema):
    id_house = fields.Int(dump_only=True)
    status_code = fields.Int(dump_only=True)
    adress = fields.Str(required=True)
    cadastr_number = fields.Str(required=True)
    id_client = fields.Int(required=True)
    is_actual = fields.Int(required=True)


class EditHouseSchema(Schema):
    status_code = fields.Int(dump_only=True)
    id_house = fields.Int(required=True)
    adress = fields.Str(required=True)
    cadastr_number = fields.Str(required=True)
    id_client = fields.Int(required=True)
    is_actual = fields.Int(required=True)


class DeleteHouseSchema(Schema):
    status_code = fields.Int(dump_only=True)
    id_house = fields.Int(required=True)
