from flask import jsonify, abort
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from db.house.get_all_houses import select_all_from_house
from logger import logger

blp = Blueprint("Get All Houses", __name__,
                description="Read All Operation Endpoint on House")


@blp.route("/get_all_houses")
class GetAllHouses(MethodView):
    @blp.response(200)
    @jwt_required(fresh=True)
    def get(self):
        result = select_all_from_house()

        if isinstance(result, str) and result.startswith("Error"):
            logger.error(f"Select From House: {result}")
            abort(400, message=result)

        logger.info(f"Select From House: Success")

        return jsonify(result), 200

    @blp.response(405)
    @jwt_required(fresh=True)
    def post(self, data):
        abort(405, message="Method is not allowed")

    @blp.response(405)
    @jwt_required(fresh=True)
    def put(self, data):
        abort(405, message="Method is not allowed")

    @blp.response(405)
    @jwt_required(fresh=True)
    def delete(self, data):
        abort(405, message="Method is not allowed")
