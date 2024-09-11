from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from db.organization.get_all_organizations import select_all_from_organization
from logger import logger

blp = Blueprint("Get All Organizations", __name__,
                description="Read All Operation Endpoint on Organization")


@blp.route("/get_all_organizations")
class GetAllOrganizations(MethodView):
    @blp.response(200)
    @jwt_required(fresh=True)
    def get(self):
        result = select_all_from_organization()

        if isinstance(result, str) and result.startswith("Error"):
            logger.error(f"Select From Organization: {result}")
            abort(400, message=result)

        logger.info(f"Select From Organization: Success")

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
