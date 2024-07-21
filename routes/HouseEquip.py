from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from CRUD.HouseEquip.HouseEquipInsert import insert_in_HouseEquip
from CRUD.HouseEquip.HouseEquipUpdate import update_in_HouseEquip
from CRUD.HouseEquip.HouseEquipDelete import delete_from_HouseEquip
from Schemas.HouseEquipSchema import AddHouseEquipSchema, EditHouseEquipSchema, DeleteHouseEquipSchema
from Schemas.ResponseSchema import AddSchema, EditDeleteSchema
from logger import logger

blp = Blueprint("HouseEquip", __name__,
                description="CRUD Operations on HouseEquip")


@blp.route("/house_equip")
class HouseEquip(MethodView):
    @blp.response(405)
    def get(self):
        abort(405, message="Method is not allowed")

    @blp.arguments(AddHouseEquipSchema)
    @blp.response(200, AddSchema)
    def post(self, data):
        id = insert_in_HouseEquip(**data)

        logger.info(f"Insert In HouseEquip: Success; ID: {id}")

        return jsonify({'status_code': 200, 'id_house_equip': id}), 200

    @blp.arguments(EditHouseEquipSchema)
    @blp.response(200, EditDeleteSchema)
    def put(self, data):
        if update_in_HouseEquip(**data) == "ERROR":
            logger.error("Update In HouseEquip: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        logger.info(f"Update In HouseEquip: Success")

        return jsonify({'status_code': 200}), 200

    @blp.arguments(DeleteHouseEquipSchema)
    @blp.response(200, EditDeleteSchema)
    def delete(self, data):
        if delete_from_HouseEquip(**data) == "ERROR":
            logger.error("Delete From HouseEquip: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        logger.info(f"Delete From HouseEquip: Success")

        return jsonify({'status_code': 200}), 200
