from flask import Flask
from data import db_session, items_api
import logging
from configparser import ConfigParser

db_session.global_init("app/db/offers.db")
app = Flask(__name__)

app.register_blueprint(items_api.blueprint)

app.logger.setLevel(logging.INFO)

config = ConfigParser()
config.read("settings.ini")
app.config["SECRET_KEY"] = config.get("settings", "secret_key")


@app.route('/')
def hello_world():
    return 'Hello World!'


def main():
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
