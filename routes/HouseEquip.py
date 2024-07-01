from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import crud
import validate_data as vd

# Спрятать
DADATA_TOKEN = "030304aa17b5f2adfda47289fa7030f73513f8b7"
DADATA_SECRET = "1fcf05efb6b0521fe6cbbc4f2dcb1a211406e91a"

blp = Blueprint("HouseEquip", __name__,
                description="CRUD Operations on HouseEquip")


@blp.route("/house_equip")
class HouseEquip(MethodView):
    def get(self):
        abort(405, message="Method is not allowed")

    def post(self):
        data = request.get_json(force=True)

        is_valid, validate_message = vd.validate_house_equip_add_data(data)
        if not is_valid:
            # app.logger.error("Insert In HouseEquip: Validation failed")
            # return jsonify({'status_code': 400, 'message': validate_message}), 400
            abort(400, message=validate_message)

        id = crud.insert_in_HouseEquip(**data)

        # app.logger.info(f"Insert In HouseEquip: Success; ID: {id}")

        return jsonify({'status_code': 200, 'id_house_equip': id}), 200

    def put(self):
        data = request.get_json(force=True)

        is_valid, validate_message = vd.validate_house_equip_edit_data(data)
        if not is_valid:
            # app.logger.error("Update In HouseEquip: Validation failed")
            # return jsonify({'status_code': 400, 'message': validate_message}), 400
            abort(400, message=validate_message)

        if crud.update_in_HouseEquip(**data) == "ERROR":
            # app.logger.error("Update In HouseEquip: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Update In HouseEquip: Success")

        return jsonify({'status_code': 200}), 200

    def delete(self):
        data = request.get_json(force=True)

        is_valid, validate_message = vd.validate_house_equip_delete_data(data)
        if not is_valid:
            # app.logger.error("Delete From HouseEquip: Validation failed")
            # return jsonify({'status_code': 400, 'message': validate_message}), 400
            abort(400, message=validate_message)

        if crud.delete_from_HouseEquip(**data) == "ERROR":
            # app.logger.error("Delete From HouseEquip: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Delete From HouseEquip: Success")

        return jsonify({'status_code': 200}), 200
