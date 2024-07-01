from flask import Flask
from flask_smorest import Api

from routes.Person import blp as PersonBlueprint
from routes.Organization import blp as OrganizationBlueprint
from routes.House import blp as HouseBlueprint
from routes.HouseEquip import blp as HouseEquipBlueprint

app = Flask(__name__)

app.config["API_TITLE"] = "GGS DB REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(PersonBlueprint)
api.register_blueprint(OrganizationBlueprint)
api.register_blueprint(HouseBlueprint)
api.register_blueprint(HouseEquipBlueprint)
