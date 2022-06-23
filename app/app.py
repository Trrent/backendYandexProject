from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from data import db_session, items_api
import logging
from configparser import ConfigParser

db_session.global_init("db/offers.db")
app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False
app.register_blueprint(items_api.blueprint)

app.logger.setLevel(logging.INFO)

config = ConfigParser()
config.read("settings.ini")
app.config["SECRET_KEY"] = config.get("settings", "secret_key")

SWAGGER_URL = '/docs'
API_URL = '/static/openapi.yaml'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Mega Market Open API'
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
