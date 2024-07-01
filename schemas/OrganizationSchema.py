from marshmallow import Schema, fields


class AddOrganizationSchema(Schema):
    id_organization = fields.Int(dump_only=True)
    status_code = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    adress_jur = fields.Str(required=True)
    adress_fact = fields.Str(required=True)
    remark = fields.Str(required=True)
    inn = fields.Str(required=True)
    kpp = fields.Str(required=True)
    from_1c = fields.Int(required=True)
    bik = fields.Str(required=False)
    korr_acc = fields.Str(required=False)
    calc_acc = fields.Str(required=False)
    bank = fields.Str(required=False)
    ogrn = fields.Str(required=False)


class EditOrganizationSchema(Schema):
    organization_id = fields.Int(required=True)
    status_code = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    from_1c = fields.Int(required=True)
    zip_code_jur = fields.Str(required=False)
    zip_code_fact = fields.Str(required=False)
    adress_jur = fields.Str(required=False)
    adress_fact = fields.Str(required=False)
    remark = fields.Str(required=False)
    inn = fields.Str(required=False)
    kpp = fields.Str(required=False)
    bik = fields.Str(required=False)
    korr_acc = fields.Str(required=False)
    calc_acc = fields.Str(required=False)
    bank = fields.Str(required=False)
    ogrn = fields.Str(required=False)


class DeleteOrganizationSchema(Schema):
    id_organization = fields.Int(required=True)
    status_code = fields.Int(dump_only=True)
