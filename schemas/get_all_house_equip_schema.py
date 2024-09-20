from marshmallow import Schema, fields


class GetAllHouseEquipSchema(Schema):
    id_house = fields.Int(required=False, load_only=True)
