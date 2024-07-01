from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import crud
import validate_data as vd
# import logging

blp = Blueprint("Person", __name__, description="CRUD Operations on Person")


@blp.route("/person")
class Person(MethodView):
    def get(self):
        abort(405, message="Method is not allowed")

    def post(self):
        data = request.get_json(force=True)

        is_valid, validate_message = vd.validate_person_add_data(data)
        if not is_valid:
            # app.logger.error("Insert In Person: Validation failed")
            # return jsonify({'status_code': 400, 'message': validate_message}), 400
            abort(400, message=validate_message)

        id = crud.insert_in_Person(**data)

        # app.logger.info(f"Insert in Person: Success; ID: {id}")

        return jsonify({'status_code': 200, 'id_client': id}), 200

    def put(self):
        data = request.get_json(force=True)

        is_valid, validate_message = vd.validate_person_edit_data(data)
        if not is_valid:
            # app.logger.error("Update In Person: Validation failed")
            # return jsonify({'status_code': 400, 'message': validate_message}), 400
            abort(400, message=validate_message)

        if crud.update_in_Person(**data) == "ERROR":
            # app.logger.error("Update In Person: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Update in Person: Success")

        return jsonify({'status_code': 200}), 200

    def delete(self):
        data = request.get_json(force=True)

        is_valid, validate_message = vd.validate_person_delete_data(data)
        if not is_valid:
            # app.logger.error("Delete From Person: Validation failed")
            # return jsonify({'status_code': 400, 'message': validate_message}), 400
            abort(400, message=validate_message)

        if crud.delete_from_Person(**data) == "ERROR":
            # app.logger.error("Delete From Person: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Delete From Person: Success")

        return jsonify({'status_code': 200}), 200
