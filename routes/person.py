from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from db.person.person_insert import insert_in_Person
from db.person.person_update import update_in_Person
from db.person.person_delete import delete_from_Person
from schemas.person_schema import AddPersonSchema, EditPersonSchema, DeletePersonSchema
from schemas.response_schema import AddSchema, EditDeleteSchema
from logger import logger

blp = Blueprint("Person", __name__, description="CRUD Operations on Person")


@blp.route("/person")
class Person(MethodView):
    @blp.response(405)
    @jwt_required()
    def get(self):
        abort(405, message="Method is not allowed")

    @jwt_required(fresh=True)
    @blp.arguments(AddPersonSchema)
    @blp.response(200, AddSchema)
    def post(self, data):
        id = insert_in_Person(**data)

        logger.info(f"Insert in Person: Success; ID: {id}")

        return jsonify({'status_code': 200, 'id_client': id}), 200

    @jwt_required(fresh=True)
    @blp.arguments(EditPersonSchema)
    @blp.response(200, EditDeleteSchema)
    def put(self, data):
        if update_in_Person(**data) == "ERROR":
            logger.error("Update In Person: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        logger.info(f"Update in Person: Success")

        return jsonify({'status_code': 200}), 200

    @jwt_required(fresh=True)
    @blp.arguments(DeletePersonSchema)
    @blp.response(200, EditDeleteSchema)
    def delete(self, data):
        if delete_from_Person(**data) == "ERROR":
            logger.error("Delete From Person: Item doesn't exist")
            # return jsonify({'status_code': 400, 'message': "Error: item doesn't exist"}), 400
            abort(400, message="Error: item doesn't exist")

        logger.info(f"Delete From Person: Success")

        return jsonify({'status_code': 200}), 200
