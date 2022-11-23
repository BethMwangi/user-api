import os

class Config:
    DEBUG = True
    API_TITLE = "Users REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://beth:Coded101@localhost/userdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    CACHE_DEFAULT_TIMEOUT = 10 * 60
