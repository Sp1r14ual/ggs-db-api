from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from schemas.token_refresh_schema import TokenRefreshSchema

blp = Blueprint("RefreshToken", __name__,
                description="Refresh Token Endpoint")


@blp.route("/refresh")
class TokenRefresh(MethodView):
    @blp.response(405)
    def get(self):
        abort(405, message="Method is not allowed")

    @blp.arguments(TokenRefreshSchema)
    @blp.response(200, TokenRefreshSchema)
    @jwt_required(refresh=True)
    def post(self, data):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity, fresh=False)
        return jsonify({'access_token': access_token})

    @blp.response(405)
    def put(self):
        abort(405, message="Method is not allowed")

    @blp.response(405)
    def delete(self):
        abort(405, message="Method is not allowed")
