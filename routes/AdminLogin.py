from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token
from Schemas.AdminSchema import AdminSchema
from Schemas.ResponseSchema import EditDeleteSchema  # ???
from Auth.AdminAuth import authenticate

from logger import logger

blp = Blueprint("Admin", __name__, description="Login operations for Admins")


@blp.route("/login")
class AdminLogin(MethodView):
    @blp.response(405)
    def get(self):
        abort(405, message="Method is not allowed")

    @blp.arguments(AdminSchema)
    @blp.response(200, EditDeleteSchema)  # ???
    def post(self, data):
        if not authenticate(data["login"]):
            abort(401, message="Invalid credentials.")

        access_token = create_access_token(identity=data["login"])
        return jsonify({"access_token": access_token}), 200

    @blp.response(405)
    def put(self):
        abort(405, message="Method is not allowed")

    @blp.response(405)
    def delete(self):
        abort(405, message="Method is not allowed")
