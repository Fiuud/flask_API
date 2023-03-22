from flask import Flask
from config.config import Config
from app.extensions import init_db, shutdown_session as shutdown
from turbo_flask import Turbo
from flask_jwt_extended import JWTManager

# инициализация Flask приложения и SQLAlchemy
app = Flask(__name__, template_folder='../app/templates')
app.config.from_object(Config)
turbo = Turbo(app)
jwt = JWTManager(app)

# Инициализация базы данных, создание сессии
init_db(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    shutdown()


# импорт маршрутов API
from app import routes
