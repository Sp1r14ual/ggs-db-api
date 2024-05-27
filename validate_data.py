def proceed_validation(data, required_fields, nullable_fields=tuple()):
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"

    for field in data:
        if (field not in required_fields) and (field not in nullable_fields):
            return False, f'Unknown field is passed: {field}'

    return True, "OK"


def validate_person_add_data(data):
    required_fields = ('family_name', 'birthdate', 'phone_number', 'name')

    nullable_fields = ('patronimic_name',
                       'pasport_serial', 'pasport_number', 'pasport_date', 'pasport_place',
                       'dep_code', 'reg_adress', 'reg_region', 'reg_raion', 'reg_city',
                       'reg_street', 'reg_house', 'postal_index', 'inn', 'ogrn', 'snils',
                       'email')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_person_edit_data(data):
    required_fields = ('client_id', 'family_name', 'name')

    nullable_fields = ('birthdate', 'phone_number', 'patronimic_name',
                       'pasport_serial', 'pasport_number', 'pasport_date', 'pasport_place',
                       'dep_code', 'reg_adress', 'reg_region', 'reg_raion', 'reg_city',
                       'reg_street', 'reg_house', 'postal_index', 'inn', 'ogrn', 'snils',
                       'email')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_person_delete_data(data):
    required_fields = ('id_client',)

    return proceed_validation(data, required_fields)


def validate_organization_add_data(data):

    required_fields = ('name', 'adress_jur', 'adress_fact',
                       'remark', 'inn', 'kpp', 'from_1c')

    nullable_fields = ('bik', 'korr_acc', 'calc_acc', 'bank', 'ogrn')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_organization_edit_data(data):
    required_fields = ('organization_id', 'name', 'from_1c')

    nullable_fields = ('adress_jur', 'zip_code_jur', 'adress_fact',
                       'zip_code_fact', 'remark',
                       'inn', 'kpp', 'bik',  'korr_acc', 'calc_acc', 'bank', 'ogrn')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_organization_delete_data(data):
    required_fields = ('id_organization',)

    return proceed_validation(data, required_fields)


def validate_house_add_data(data):
    required_fields = ('adress', 'cadastr_number', 'id_client', 'is_actual')

    nullable_fields = ()

    return proceed_validation(data, required_fields, nullable_fields)


def validate_house_edit_data(data):
    required_fields = ('town', 'district', 'street',
                       'house_number', 'corpus_number',
                       'client_id', 'is_actual', 'id_house')

    nullable_fields = ('flat_number', 'cadastr_number')

    return proceed_validation(data, required_fields, nullable_fields)


def validate_house_delete_data(data):
    required_fields = ('id_house',)

    return proceed_validation(data, required_fields)


def validate_house_equip_add_data(data):
    required_fields = ('id_house', 'id_type_house_equip',
                       'year_produce', 'remark')

    nullable_fields = ()

    return proceed_validation(data, required_fields, nullable_fields)


def validate_house_equip_edit_data(data):
    required_fields = ('house_id',
                       'id_type_house_equip', 'year_produce', 'remark', 'id_house_equip')

    nullable_fields = ()

    return proceed_validation(data, required_fields, nullable_fields)


def validate_house_equip_delete_data(data):
    required_fields = ('id_house_equip',)

    return proceed_validation(data, required_fields)
