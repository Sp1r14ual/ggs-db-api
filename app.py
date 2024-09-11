from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
import datetime
from settings import settings

from routes.person import blp as person_blueprint
from routes.organization import blp as organization_blueprint
from routes.house import blp as house_blueprint
from routes.house_equip import blp as house_equip_blueprint
from routes.admin_login import blp as admin_login_blueprint
from routes.token_refresh import blp as token_refresh_blueprint
from routes.get_all_people import blp as get_all_people_blueprint
from routes.get_all_organizations import blp as get_all_organizations_blueprint
from routes.get_all_houses import blp as get_all_houses_blueprint
from routes.get_all_house_equip import blp as get_all_house_equip_blueprint

app = Flask(__name__)

app.config["API_TITLE"] = "GGS DB REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["JWT_SECRET_KEY"] = settings.JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

jwt = JWTManager(app)

api = Api(app)

api.register_blueprint(person_blueprint)
api.register_blueprint(organization_blueprint)
api.register_blueprint(house_blueprint)
api.register_blueprint(house_equip_blueprint)
api.register_blueprint(admin_login_blueprint)
api.register_blueprint(token_refresh_blueprint)
api.register_blueprint(get_all_people_blueprint)
api.register_blueprint(get_all_organizations_blueprint)
api.register_blueprint(get_all_houses_blueprint)
api.register_blueprint(get_all_house_equip_blueprint)

if __name__ == '__main__':
    app.run(host=settings.HOST,
            port=settings.PORT, debug=True)
