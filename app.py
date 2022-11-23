import os
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

from config import Config
from extensions import db, cache
from resources.user import blp as UserBlueprint


def create_app():
    env = os.environ.get("ENV", "Development")
    if env == "Production":
        config_str = "config.ProductionConfig"
    else:
        config_str = "config.DevelopmentConfig"
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
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
    app.run(host="0.0.0.0", debug=True)
