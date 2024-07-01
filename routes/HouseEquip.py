from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import crud
from schemas.HouseEquipSchema import AddHouseEquipSchema, EditHouseEquipSchema, DeleteHouseEquipSchema

# Спрятать
DADATA_TOKEN = "030304aa17b5f2adfda47289fa7030f73513f8b7"
DADATA_SECRET = "1fcf05efb6b0521fe6cbbc4f2dcb1a211406e91a"

blp = Blueprint("HouseEquip", __name__,
                description="CRUD Operations on HouseEquip")


@blp.route("/house_equip")
class HouseEquip(MethodView):
    def get(self):
        abort(405, message="Method is not allowed")

    @blp.arguments(AddHouseEquipSchema)
    def post(self, data):
        id = crud.insert_in_HouseEquip(**data)

        # app.logger.info(f"Insert In HouseEquip: Success; ID: {id}")

        return jsonify({'status_code': 200, 'id_house_equip': id}), 200

    @blp.arguments(EditHouseEquipSchema)
    def put(self, data):
        if crud.update_in_HouseEquip(**data) == "ERROR":
            # app.logger.error("Update In HouseEquip: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Update In HouseEquip: Success")

        return jsonify({'status_code': 200}), 200

    @blp.arguments(DeleteHouseEquipSchema)
    def delete(self, data):
        if crud.delete_from_HouseEquip(**data) == "ERROR":
            # app.logger.error("Delete From HouseEquip: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Delete From HouseEquip: Success")

        return jsonify({'status_code': 200}), 200
