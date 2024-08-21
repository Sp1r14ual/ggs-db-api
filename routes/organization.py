from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from db.organization.organization_insert import insert_in_Organization
from db.organization.organization_update import update_in_Organization
from db.organization.organization_delete import delete_from_Organization
from schemas.organization_schema import AddOrganizationSchema, EditOrganizationSchema, DeleteOrganizationSchema
from schemas.response_schema import AddSchema, EditDeleteSchema
from logger import logger

blp = Blueprint("Organization", __name__,
                description="CRUD Operations on Organization")


@blp.route("/organization")
class Organization(MethodView):
    @blp.response(405)
    def get(self):
        abort(405, message="Method is not allowed")

    @jwt_required(fresh=True)
    @blp.arguments(AddOrganizationSchema)
    @blp.response(201, AddSchema)
    def post(self, data):
        id = insert_in_Organization(**data)

        logger.info(f"Insert in Organization: Success; ID: {id}")

        return jsonify({'id_organization': id}), 201

    @jwt_required(fresh=True)
    @blp.arguments(EditOrganizationSchema)
    @blp.response(200, EditDeleteSchema)
    def put(self, data):
        result = update_in_Organization(**data)
        if isinstance(result, str) and result.startswith("Error"):
            logger.error(f"Update In Organization: {result}")
            abort(400, message=result)

        logger.info(f"Update in Organization: Success")

        return jsonify({}), 200

    @jwt_required(fresh=True)
    @blp.arguments(DeleteOrganizationSchema)
    @blp.response(200, EditDeleteSchema)
    def delete(self, data):
        result = delete_from_Organization(**data)
        if isinstance(result, str) and result.startswith("Error"):
            logger.error(f"Delete From Organization: {result}")
            abort(400, message=result)

        logger.info(f"Delete From Organization: Success")

        return jsonify({}), 200
