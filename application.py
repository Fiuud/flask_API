from flask import Flask
from utils.jwt_token import jwt
from utils.turbo import turbo
from extensions.database_extension import init_db
from config import Config
from extensions.routes_extension import register_routes


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    jwt.init_app(app)
    turbo.init_app(app)
    init_db(app)

    # will move to register_config soon
    # app.config['ERROR_404_HELP'] = False

    register_routes(app)
    return app
