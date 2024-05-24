def proceed_validation(data, required_fields, nullable_fields=tuple()):
    # for field in required_fields:
    #     if field not in data:
    #         return False, f"Missing required field: {field}"

    for field in data:
        if (field not in required_fields) and (field not in nullable_fields):
            return False, f'Unknown field is passed: {field}'

    return True, "OK"


def validate_person_add_data(data):
    required_fields = ('family_name', 'name')

    nullable_fields = ('birthdate', 'phone_number', 'patronimic_name',
                       'pasport_serial', 'pasport_number', 'pasport_date', 'pasport_place',
                       'dep_code', 'reg_adress', 'reg_region', 'reg_raion', 'reg_city',
                       'reg_street', 'reg_house', 'postal_index', 'inn', 'ogrn', 'snils',
                       'email')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_person_edit_data(data):
    required_fields = ('id',)

    nullable_fields = ('family_name', 'name', 'birthdate', 'phone_number', 'patronimic_name',
                       'pasport_serial', 'pasport_number', 'pasport_date', 'pasport_place',
                       'dep_code', 'reg_adress', 'reg_region', 'reg_raion', 'reg_city',
                       'reg_street', 'reg_house', 'postal_index', 'inn', 'ogrn', 'snils',
                       'email')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_person_delete_data(data):
    required_fields = ('id',)

    return proceed_validation(data, required_fields)


def validate_organization_add_data(data):

    required_fields = ('name', 'is_coop', 'is_pir', 'is_smr_gvd_gnd', 'is_smr_vdgo',
                       'is_to_gvd_gnd', 'from_1c', 'to_rg', 'to_ggs', 'to_gss', 'to_ggsi', 'to_ggss', 'to_rgs')

    nullable_fields = ('adress_jur', 'zip_code_jur', 'adress_fact',
                       'zip_code_fact', 'remark', 'inn', 'bik',  'korr_acc', 'calc_acc', 'bank', 'ogrn')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_organization_edit_data(data):
    required_fields = ('id',)

    nullable_fields = ('name', 'adress_jur', 'zip_code_jur', 'adress_fact',
                       'zip_code_fact', 'remark',
                       'inn', 'bik',  'korr_acc', 'calc_acc', 'bank', 'ogrn',
                       'is_coop', 'is_pir', 'is_smr_gvd_gnd', 'is_smr_vdgo',
                       'is_to_gvd_gnd', 'from_1c', 'to_rg', 'to_ggs', 'to_gss',
                       'to_ggsi', 'to_ggss', 'to_rgs')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_organization_delete_data(data):
    required_fields = ('id',)

    return proceed_validation(data, required_fields)


def validate_house_add_data(data):
    required_fields = ()

    nullable_fields = ('cadastr_number',)

    return proceed_validation(data, required_fields, nullable_fields)


def validate_house_edit_data(data):
    required_fields = ('id',)

    nullable_fields = ('cadastr_number',)

    return proceed_validation(data, required_fields, nullable_fields)


def validate_house_delete_data(data):
    required_fields = ('id',)

    return proceed_validation(data, required_fields)


def validate_house_equip_add_data(data):
    required_fields = ()

    nullable_fields = ('id_abonent', 'id_house',
                       'id_type_house_equip', 'year_produce', 'remark')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_house_equip_edit_data(data):
    required_fields = ('id',)

    nullable_fields = ('id_abonent', 'id_house',
                       'id_type_house_equip', 'year_produce', 'remark')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_house_equip_delete_data(data):
    required_fields = ('id',)

    return proceed_validation(data, required_fields)
