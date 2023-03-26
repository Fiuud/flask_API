from flask import Flask
from utils import jwt, turbo, login_manager
from extensions.database_extension import init_db
from config import Config
from extensions.routes_extension import register_routes


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    jwt.init_app(app)
    turbo.init_app(app)
    login_manager.init_app(app)

    init_db(app)
    register_routes(app)

    # will move to register_config soon
    # app.config['ERROR_404_HELP'] = False

    return app
