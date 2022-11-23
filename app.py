from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

from config import Config
from extensions import db, cache
from resources.user import blp as UserBlueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["API_TITLE"] = "Users REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql+psycopg2://beth:Coded101@localhost/userdb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    cache.init_app(app)


def register_resources(app):
    api = Api(app)
    api.register_blueprint(UserBlueprint)


if __name__ == "__main__":
    app = create_app()
    app.run()
