from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from dadata import Dadata
from settings import DADATA_TOKEN, DADATA_SECRET
from db.house.house_insert import insert_in_House
from db.house.house_update import update_in_House
from db.house.house_delete import delete_from_House
from schemas.house_schema import AddHouseSchema, EditHouseSchema, DeleteHouseSchema
from schemas.response_schema import AddSchema, EditDeleteSchema
from logger import logger

blp = Blueprint("House", __name__, description="CRUD Operations on House")


@blp.route("/house")
class House(MethodView):
    @blp.response(405)
    def get(self):
        abort(405, message="Method is not allowed")

    @jwt_required()
    @blp.arguments(AddHouseSchema)
    @blp.response(200, AddSchema)
    def post(self, data):
        global parsed_data
        parsed_data = dict()

        with Dadata(DADATA_TOKEN, DADATA_SECRET) as dd:
            parsed_address = dd.clean("address", data["adress"])
            parsed_data["town"] = parsed_address["city"]
            parsed_data["district"] = parsed_address["city_district"]
            parsed_data["street"] = parsed_address["street"]
            parsed_data["house_number"] = parsed_address["house"]
            parsed_data["corpus_number"] = parsed_address["block"]
            parsed_data["flat_number"] = parsed_address["flat"]

        # id = insert_in_House(**data)
        id = insert_in_House(**dict(data, **parsed_data))

        if id == "ERROR":
            logger.error("Insert In House: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        logger.info(f"Insert In House: Success; ID: {id}")

        return jsonify({'status_code': 200, 'id_house': id}), 200

    @jwt_required()
    @blp.arguments(EditHouseSchema)
    @blp.response(200, EditDeleteSchema)
    def put(self, data):
        global parsed_data
        parsed_data = dict()

        with Dadata(DADATA_TOKEN, DADATA_SECRET) as dd:
            parsed_address = dd.clean("address", data["adress"])
            parsed_data["town"] = parsed_address["city"]
            parsed_data["district"] = parsed_address["city_district"]
            parsed_data["street"] = parsed_address["street"]
            parsed_data["house_number"] = parsed_address["house"]
            parsed_data["corpus_number"] = parsed_address["block"]
            parsed_data["flat_number"] = parsed_address["flat"]

        if update_in_House(**dict(data, **parsed_data)) == "ERROR":
            logger.error("Update In House: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        logger.info(f"Update In House: Success")

        return jsonify({'status_code': 200}), 200

    @jwt_required()
    @blp.arguments(DeleteHouseSchema)
    @blp.response(200, EditDeleteSchema)
    def delete(self, data):
        if delete_from_House(**data) == "ERROR":
            logger.error("Delete From House: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        logger.info(f"Delete From House: Success")

        return jsonify({'status_code': 200}), 200
