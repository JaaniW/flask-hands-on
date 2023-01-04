from flask import current_app as app
from config import Config

config = Config()

@app.route("/")
def route_base():
    return 'Hello World!'
