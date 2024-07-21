from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
import secrets

from Routes.Person import blp as PersonBlueprint
from Routes.Organization import blp as OrganizationBlueprint
from Routes.House import blp as HouseBlueprint
from Routes.HouseEquip import blp as HouseEquipBlueprint
from Routes.AdminLogin import blp as AdminLoginBlueprint

app = Flask(__name__)

app.config["API_TITLE"] = "GGS DB REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["JWT_SECRET_KEY"] = str(secrets.SystemRandom().getrandbits(128))

jwt = JWTManager(app)

api = Api(app)

api.register_blueprint(PersonBlueprint)
api.register_blueprint(OrganizationBlueprint)
api.register_blueprint(HouseBlueprint)
api.register_blueprint(HouseEquipBlueprint)
api.register_blueprint(AdminLoginBlueprint)
