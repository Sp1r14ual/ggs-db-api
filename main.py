from flask import Flask, request, jsonify
import crud
import validate_data as vd

app = Flask(__name__)


################### Person TABLE -> ###################


@app.route('/add_person', methods=['POST'])
def add_person():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_person_add_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    id = crud.insert_in_Person(**data)

    return jsonify({'status_code': 200, 'id_client': id}), 200


@app.route('/edit_person', methods=['POST'])
def edit_person():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_person_edit_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    crud.update_in_Person(**data)

    # Что должно возвращаться при редактировании? В мануале не указано
    return jsonify({'status_code': 200}), 200


@app.route('/delete_person', methods=['POST'])
def delete_person():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_person_delete_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    crud.delete_from_Person(**data)

    # Что должно возвращаться при редактировании? В мануале не указано
    return jsonify({'status_code': 200}), 200


################### <- Person TABLE  |  Organization TABLE -> ###################


@app.route('/add_organization', methods=['POST'])
def add_organization():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_organization_add_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    id = crud.insert_in_Organization(**data)

    return jsonify({'status_code': 200, 'id_organization': id}), 200


@app.route('/edit_organization', methods=['POST'])
def edit_organization():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_organization_edit_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    crud.update_in_Organization(**data)

    # Что должно возвращаться при редактировании? В мануале не указано
    return jsonify({'status_code': 200}), 200


@app.route('/delete_organization', methods=['POST'])
def delete_organization():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_organization_delete_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    crud.delete_from_Organization(**data)

    # Что должно возвращаться при редактировании? В мануале не указано
    return jsonify({'status_code': 200}), 200


################### <- Organization TABLE  |  House TABLE -> ###################


@app.route('/add_house', methods=['POST'])
def add_house():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_house_add_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    id = crud.insert_in_House(**data)

    return jsonify({'status_code': 200, 'id_house': id}), 200


@app.route('/edit_house', methods=['POST'])
def edit_house():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_house_edit_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    crud.update_in_House(**data)

    # Что должно возвращаться при редактировании? В мануале не указано
    return jsonify({'status_code': 200}), 200


@app.route('/delete_house', methods=['POST'])
def delete_house():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_house_delete_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    crud.delete_from_House(**data)

    # Что должно возвращаться при редактировании? В мануале не указано
    return jsonify({'status_code': 200}), 200


################### <- House TABLE  |  House Equip TABLE -> ###################


@app.route('/add_house_equip', methods=['POST'])
def add_house_equip():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_house_equip_add_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    id = crud.insert_in_HouseEquip(**data)

    return jsonify({'status_code': 200, 'id_house_equip': id}), 200


@app.route('/edit_house_equip', methods=['POST'])
def edit_house_equip():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_house_equip_edit_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    crud.update_in_HouseEquip(**data)

    # Что должно возвращаться при редактировании? В мануале не указано
    return jsonify({'status_code': 200}), 200


@app.route('/delete_house_equip', methods=['POST'])
def delete_house_equip():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_house_equip_delete_data(data)
    if not is_valid:
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    crud.delete_from_HouseEquip(**data)

    # Что должно возвращаться при редактировании? В мануале не указано
    return jsonify({'status_code': 200}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")
