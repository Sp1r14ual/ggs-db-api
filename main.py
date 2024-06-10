from flask import Flask, request, jsonify
from dadata import Dadata
import crud
import validate_data as vd
import logging

DADATA_TOKEN = "030304aa17b5f2adfda47289fa7030f73513f8b7"
DADATA_SECRET = "1fcf05efb6b0521fe6cbbc4f2dcb1a211406e91a"


app = Flask(__name__)


################### Person TABLE -> ###################


@app.route('/add_person', methods=['POST'])
def add_person():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_person_add_data(data)
    if not is_valid:
        app.logger.error("Insert In Person: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    id = crud.insert_in_Person(**data)

    app.logger.info(f"Insert in Person: Success; ID: {id}")

    return jsonify({'status_code': 200, 'id_client': id}), 200


@app.route('/edit_person', methods=['PUT'])
def edit_person():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_person_edit_data(data)
    if not is_valid:
        app.logger.error("Update In Person: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    if crud.update_in_Person(**data) == "ERROR":
        app.logger.error("Update In Person: Item doesn't exist")
        return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400

    app.logger.info(f"Update in Person: Success")

    return jsonify({'status_code': 200}), 200


@app.route('/delete_person', methods=['DELETE'])
def delete_person():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_person_delete_data(data)
    if not is_valid:
        app.logger.error("Delete From Person: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    if crud.delete_from_Person(**data) == "ERROR":
        app.logger.error("Delete From Person: Item doesn't exist")
        return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400

    app.logger.info(f"Delete From Person: Success")

    return jsonify({'status_code': 200}), 200


################### <- Person TABLE  |  Organization TABLE -> ###################


@app.route('/add_organization', methods=['POST'])
def add_organization():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_organization_add_data(data)
    if not is_valid:
        app.logger.error("Insert In Organization: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    id = crud.insert_in_Organization(**data)

    app.logger.info(f"Insert in Organization: Success; ID: {id}")

    return jsonify({'status_code': 200, 'id_organization': id}), 200


@app.route('/edit_organization', methods=['PUT'])
def edit_organization():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_organization_edit_data(data)
    if not is_valid:
        app.logger.error("Update In Organization: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    if crud.update_in_Organization(**data) == "ERROR":
        app.logger.error("Update In Organization: Item doesn't exist")
        return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400

    app.logger.info(f"Update in Organization: Success")

    return jsonify({'status_code': 200}), 200


@app.route('/delete_organization', methods=['DELETE'])
def delete_organization():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_organization_delete_data(data)
    if not is_valid:
        app.logger.error("Delete From Organization: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    if crud.delete_from_Organization(**data) == "ERROR":
        app.logger.error("Delete From Organization: Item doesn't exist")
        return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400

    app.logger.info(f"Delete From Organization: Success")

    return jsonify({'status_code': 200}), 200


################### <- Organization TABLE  |  House TABLE -> ###################


@app.route('/add_house', methods=['POST'])
def add_house():

    data = request.get_json(force=True)

    global parsed_data
    parsed_data = dict()

    is_valid, validate_message = vd.validate_house_add_data(data)
    if not is_valid:
        app.logger.error("Insert In House: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    with Dadata(DADATA_TOKEN, DADATA_SECRET) as dd:
        parsed_address = dd.clean("address", data["adress"])
        parsed_data["town"] = parsed_address["city"]
        parsed_data["district"] = parsed_address["city_district"]
        parsed_data["street"] = parsed_address["street"]
        parsed_data["house_number"] = parsed_address["house"]
        parsed_data["corpus_number"] = parsed_address["block"]
        parsed_data["flat_number"] = parsed_address["flat"]

    # id = crud.insert_in_House(**data)
    id = crud.insert_in_House(**dict(data, **parsed_data))

    if id == "ERROR":
        app.logger.error("Insert In House: Item doesn't exist")
        return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400

    app.logger.info(f"Insert In House: Success; ID: {id}")

    return jsonify({'status_code': 200, 'id_house': id}), 200


@app.route('/edit_house', methods=['PUT'])
def edit_house():

    data = request.get_json(force=True)

    global parsed_data
    parsed_data = dict()

    is_valid, validate_message = vd.validate_house_edit_data(data)
    if not is_valid:
        app.logger.error("Update In House: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    with Dadata(DADATA_TOKEN, DADATA_SECRET) as dd:
        parsed_address = dd.clean("address", data["adress"])
        parsed_data["town"] = parsed_address["city"]
        parsed_data["district"] = parsed_address["city_district"]
        parsed_data["street"] = parsed_address["street"]
        parsed_data["house_number"] = parsed_address["house"]
        parsed_data["corpus_number"] = parsed_address["block"]
        parsed_data["flat_number"] = parsed_address["flat"]

    if crud.update_in_House(**dict(data, **parsed_data)) == "ERROR":
        app.logger.error("Update In House: Item doesn't exist")
        return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400

    app.logger.info(f"Update In House: Success")

    return jsonify({'status_code': 200}), 200


@app.route('/delete_house', methods=['DELETE'])
def delete_house():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_house_delete_data(data)
    if not is_valid:
        app.logger.error("Delete From House: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    if crud.delete_from_House(**data) == "ERROR":
        app.logger.error("Delete From House: Item doesn't exist")
        return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400

    app.logger.info(f"Delete From House: Success")

    return jsonify({'status_code': 200}), 200


################### <- House TABLE  |  House Equip TABLE -> ###################


@app.route('/add_house_equip', methods=['POST'])
def add_house_equip():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_house_equip_add_data(data)
    if not is_valid:
        app.logger.error("Insert In HouseEquip: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    id = crud.insert_in_HouseEquip(**data)

    app.logger.info(f"Insert In HouseEquip: Success; ID: {id}")

    return jsonify({'status_code': 200, 'id_house_equip': id}), 200


@app.route('/edit_house_equip', methods=['PUT'])
def edit_house_equip():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_house_equip_edit_data(data)
    if not is_valid:
        app.logger.error("Update In HouseEquip: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    if crud.update_in_HouseEquip(**data) == "ERROR":
        app.logger.error("Update In HouseEquip: Item doesn't exist")
        return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400

    app.logger.info(f"Update In HouseEquip: Success")

    return jsonify({'status_code': 200}), 200


@app.route('/delete_house_equip', methods=['DELETE'])
def delete_house_equip():

    data = request.get_json(force=True)

    is_valid, validate_message = vd.validate_house_equip_delete_data(data)
    if not is_valid:
        app.logger.error("Delete From HouseEquip: Validation failed")
        return jsonify({'status_code': 400, 'message': validate_message}), 400

    if crud.delete_from_HouseEquip(**data) == "ERROR":
        app.logger.error("Delete From HouseEquip: Item doesn't exist")
        return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400

    app.logger.info(f"Delete From HouseEquip: Success")

    return jsonify({'status_code': 200}), 200


if __name__ == '__main__':
    logging.basicConfig(filename='record.log',
                        level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    app.run(host="0.0.0.0")
