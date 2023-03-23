from flask import Blueprint, request

from services import login_service

login_route = Blueprint('login_route', __name__)


# маршрут для авторизации сканера и получения токена доступа
@login_route.route('/login', methods=['POST'])
def scanner_login():
    return login_service.scanner_login(request.json)
