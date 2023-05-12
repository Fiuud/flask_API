from flask import Blueprint
from flask_login import login_required
import pprint
from services import teacher_auth_service

teacher_auth_route = Blueprint('teacher_auth', __name__, url_prefix='/teacher')


# маршрут для авторизации сканера и получения токена доступа
@teacher_auth_route.route('/login', methods=['GET', 'POST'])
def teacher_login():
    # from extensions.database_extension import db_session
    # from models import Event
    # from sqlalchemy import cast, Text
    # from sqlalchemy.sql.operators import like_op
    # pprint.pprint(db_session.query(Event.recurrence).filter(cast(Event.recurrence, Text).like('%BYDAY=WE%')).all())
    return teacher_auth_service.teacher_login()


@teacher_auth_route.route('/registration', methods=['GET', 'POST'])
def teacher_reg():
    return teacher_auth_service.teacher_reg()


@teacher_auth_route.route('/logout')
@login_required
def logout():
    return teacher_auth_service.logout_teacher()
