from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import crud
from schemas.OrganizationSchema import AddOrganizationSchema, EditOrganizationSchema, DeleteOrganizationSchema
from schemas.ResponseSchema import AddSchema, EditDeleteSchema

blp = Blueprint("Organization", __name__,
                description="CRUD Operations on Organization")


@blp.route("/organization")
class Organization(MethodView):
    @blp.response(405)
    def get(self):
        abort(405, message="Method is not allowed")

    @blp.arguments(AddOrganizationSchema)
    @blp.response(200, AddSchema)
    def post(self, data):
        id = crud.insert_in_Organization(**data)

        # app.logger.info(f"Insert in Organization: Success; ID: {id}")

        return jsonify({'status_code': 200, 'id_organization': id}), 200

    @blp.arguments(EditOrganizationSchema)
    @blp.response(200, EditDeleteSchema)
    def put(self, data):
        if crud.update_in_Organization(**data) == "ERROR":
            # app.logger.error("Update In Organization: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Update in Organization: Success")

        return jsonify({'status_code': 200}), 200

    @blp.arguments(DeleteOrganizationSchema)
    @blp.response(200, EditDeleteSchema)
    def delete(self, data):
        if crud.delete_from_Organization(**data) == "ERROR":
            # app.logger.error("Delete From Organization: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Delete From Organization: Success")

        return jsonify({'status_code': 200}), 200
