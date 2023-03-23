from datetime import timedelta

from flask import jsonify, abort
from flask_jwt_extended import create_access_token

from extensions.database_extension import db_session
from models import Event
from config import Config


def scanner_login(request):
    if not request \
            or 'audience' not in request \
            or 'password' not in request:
        abort(400)

    audience, password = request.values()

    if not db_session.query(Event).filter(
            Event.location.like(f'%{audience}%')) and not password == Config.AUDIENCE_PASS:
        return jsonify({'message': 'Неверные учетные данные'}), 401

    # Создаём токен доуступа
    expires_delta = timedelta(hours=2)
    access_token = create_access_token(identity={'audience': audience}, expires_delta=expires_delta)

    return jsonify({'access_token': access_token}), 200
