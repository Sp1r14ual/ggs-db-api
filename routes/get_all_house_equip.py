from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from db.house_equip.get_all_house_equip import select_all_from_house_equip_by_id
from schemas.get_all_house_equip_schema import GetAllHouseEquipSchema
from logger import logger

blp = Blueprint("Get All House Equip", __name__,
                description="Read All Operation Endpoint on House Equip")


@blp.route("/get_all_house_equip")
class GetAllHouseEquip(MethodView):
    @jwt_required(fresh=True)
    @blp.arguments(GetAllHouseEquipSchema)
    @blp.response(200)
    def post(self, data):
        result = select_all_from_house_equip_by_id(**data)

        if isinstance(result, str) and result.startswith("Error"):
            logger.error(f"Select From House Equip: {result}")
            abort(400, message=result)

        logger.info(f"Select From House Equip: Success")

        return jsonify(result), 200

    @blp.response(405)
    @jwt_required(fresh=True)
    def get(self):
        abort(405, message="Method is not allowed")

    @blp.response(405)
    @jwt_required(fresh=True)
    def put(self, data):
        abort(405, message="Method is not allowed")

    @blp.response(405)
    @jwt_required(fresh=True)
    def delete(self, data):
        abort(405, message="Method is not allowed")
