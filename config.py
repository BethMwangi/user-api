class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://beth:Coded101@localhost/userdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_TITLE = "Stores REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL= "https://cdnjsdelivrnet/npm/swagger-ui-dist/"
    PROPAGATE_EXCEPTIONS = True