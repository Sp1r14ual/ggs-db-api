from marshmallow import Schema, fields


class AddHouseEquipSchema(Schema):
    id_house_equip = fields.Int(dump_only=True)
    status_code = fields.Int(dump_only=True)
    id_house = fields.Int(required=True)
    id_type_house_equip = fields.Int(required=True)
    year_produce = fields.Int(required=True)
    remark = fields.Str(required=True)


class EditHouseEquipSchema(Schema):
    status_code = fields.Int(dump_only=True)
    house_id = fields.Int(required=True)
    id_type_house_equip = fields.Int(required=True)
    year_produce = fields.Int(required=True)
    remark = fields.Str(required=True)
    id_house_equip = fields.Int(required=True)


class DeleteHouseEquipSchema(Schema):
    status_code = fields.Int(dump_only=True)
    id_house_equip = fields.Int(required=True)
