from flask import Blueprint, request

from services import scanner_login_service

scanner_login_route = Blueprint('scanner_login', __name__, url_prefix='/scanner')


# маршрут для авторизации сканера и получения токена доступа
@scanner_login_route.route('/login', methods=['POST'])
def scanner_login():
    return scanner_login_service.scanner_login(request.json)
