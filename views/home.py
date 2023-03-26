from flask import Blueprint, request
from flask_login import login_required, current_user

from services import home_service

home_route = Blueprint('home', __name__)


# маршрут для главной страницы
@home_route.route('/')
@login_required
def index():
    return home_service.index()
