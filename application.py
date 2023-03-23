from flask import Flask

from config import Config
from extensions.routes_extension import register_routes


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)



    # will move to register_config soon
    # app.config['ERROR_404_HELP'] = False

    register_routes(app)
    return app
