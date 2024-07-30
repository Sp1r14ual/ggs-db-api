from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
import secrets

from routes.person import blp as person_blueprint
from routes.organization import blp as organization_blueprint
from routes.house import blp as house_blueprint
from routes.house_equip import blp as house_equip_blueprint
from routes.admin_login import blp as admin_login_blueprint

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

api.register_blueprint(person_blueprint)
api.register_blueprint(organization_blueprint)
api.register_blueprint(house_blueprint)
api.register_blueprint(house_equip_blueprint)
api.register_blueprint(admin_login_blueprint)
