from flask import Flask
from flask_migrate import Migrate

# from application.database.models.models import db


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    with app.app_context():
        from . import routes  # Import routes

        # db.init_app(app)
        # db.app = app
        #migrate = Migrate(app, db)
        # db.create_all()  # Create sql tables for our data models

        return app


app = create_app()

