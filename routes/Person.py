from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import crud
from schemas.PersonSchema import AddPersonSchema, EditPersonSchema, DeletePersonSchema
# import logging

blp = Blueprint("Person", __name__, description="CRUD Operations on Person")


@blp.route("/person")
class Person(MethodView):
    def get(self):
        abort(405, message="Method is not allowed")

    @blp.arguments(AddPersonSchema)
    def post(self, data):
        id = crud.insert_in_Person(**data)

        # app.logger.info(f"Insert in Person: Success; ID: {id}")

        return jsonify({'status_code': 200, 'id_client': id}), 200

    @blp.arguments(EditPersonSchema)
    def put(self, data):
        if crud.update_in_Person(**data) == "ERROR":
            # app.logger.error("Update In Person: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Update in Person: Success")

        return jsonify({'status_code': 200}), 200

    @blp.arguments(DeletePersonSchema)
    def delete(self, data):
        if crud.delete_from_Person(**data) == "ERROR":
            # app.logger.error("Delete From Person: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        # app.logger.info(f"Delete From Person: Success")

        return jsonify({'status_code': 200}), 200
