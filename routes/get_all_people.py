from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from db.person.get_all_people import select_all_from_person
from logger import logger

blp = Blueprint("Get All People", __name__,
                description="Read All Operation Endpoint on Person")


@blp.route("/get_all_people")
class GetAllPeople(MethodView):
    @blp.response(200)
    @jwt_required(fresh=True)
    def get(self):
        result = select_all_from_person()

        if isinstance(result, str) and result.startswith("Error"):
            logger.error(f"Select From Person: {result}")
            abort(400, message=result)

        logger.info(f"Select From Person: Success")

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
    def put(self, data):
        abort(405, message="Method is not allowed")
