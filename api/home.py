from flask import Blueprint, request

from services import home_service

home_route = Blueprint('home_route', __name__)


# маршрут для главной страницы
@home_route.route('/')
def index():
    return home_service.index()
