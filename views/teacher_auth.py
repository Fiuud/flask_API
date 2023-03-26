from flask import Blueprint
from flask_login import login_required

from services import teacher_auth_service

teacher_auth_route = Blueprint('teacher_auth', __name__, url_prefix='/teacher')


# маршрут для авторизации сканера и получения токена доступа
@teacher_auth_route.route('/login', methods=['GET', 'POST'])
def teacher_login():
    return teacher_auth_service.teacher_login()


@teacher_auth_route.route('/registration', methods=['GET', 'POST'])
def teacher_reg():
    return teacher_auth_service.teacher_reg()


@teacher_auth_route.route('/logout')
@login_required
def logout():
    return teacher_auth_service.logout_teacher()
