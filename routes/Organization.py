from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import crud
import validate_data as vd

blp = Blueprint("Organization", __name__,
                description="CRUD Operations on Organization")


@blp.route("/organization")
class Organization(MethodView):
    def get(self):
        abort(405, message="Method is not allowed")

    def post(self):
        data = request.get_json(force=True)

        is_valid, validate_message = vd.validate_organization_add_data(data)
        if not is_valid:
            # app.logger.error("Insert In Organization: Validation failed")
            # return jsonify({'status_code': 400, 'message': validate_message}), 400
            abort(400, message=validate_message)

        id = crud.insert_in_Organization(**data)

        # app.logger.info(f"Insert in Organization: Success; ID: {id}")

        return jsonify({'status_code': 200, 'id_organization': id}), 200

    def put(self):
        data = request.get_json(force=True)

        is_valid, validate_message = vd.validate_organization_edit_data(data)
        if not is_valid:
            # app.logger.error("Update In Organization: Validation failed")
            # return jsonify({'status_code': 400, 'message': validate_message}), 400
            abort(400, message=validate_message)

        if crud.update_in_Organization(**data) == "ERROR":
            # app.logger.error("Update In Organization: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Update in Organization: Success")

        return jsonify({'status_code': 200}), 200

    def delete(self):
        data = request.get_json(force=True)

        is_valid, validate_message = vd.validate_organization_delete_data(data)
        if not is_valid:
            # app.logger.error("Delete From Organization: Validation failed")
            # return jsonify({'status_code': 400, 'message': validate_message}), 400
            abort(400, message=validate_message)

        if crud.delete_from_Organization(**data) == "ERROR":
            # app.logger.error("Delete From Organization: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Delete From Organization: Success")

        return jsonify({'status_code': 200}), 200
