import os

class Config:
    DEBUG = False
    API_TITLE = "Users REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    CACHE_DEFAULT_TIMEOUT = 10 * 60
    CACHE_TYPE = 'simple'


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'my-secret-key'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://beth:Coded101@localhost/userdb"


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')