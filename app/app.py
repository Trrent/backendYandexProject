from flask import Flask
from data import db_session
import logging
from configparser import ConfigParser

db_session.global_init("app/db/offers.db")
app = Flask(__name__)
app.logger.setLevel(logging.INFO)

config = ConfigParser()
config.read("settings.ini")
app.config["SECRET_KEY"] = config.get("settings", "secret_key")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
