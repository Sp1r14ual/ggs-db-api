from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from db.organization.get_all_organizations import select_all_from_organization

blp = Blueprint("Get All Organizations", __name__,
                description="Read All Operation Endpoint on Organization")


@blp.route("/get_all_organizations")
class GetAllOrganizations(MethodView):
    @blp.response(200)
    @jwt_required(fresh=True)
    def get(self):
        return jsonify(select_all_from_organization()), 200

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
