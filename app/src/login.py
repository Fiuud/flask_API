from datetime import timedelta

from flask import jsonify, abort
from flask_jwt_extended import create_access_token

from app.extensions import db_session
from app.models import Event


def scanner_login(request):
    if not request \
            or 'audience' not in request \
            or 'password' not in request \
            or 'weekType' not in request \
            or request['weekType'] not in [0, 1, 2]:
        abort(400)

    audience, password, week_type = request.values()

    # TODO: дописать проверку пароля
    if not db_session.query(Event).filter(Event.location.like(f'%{audience}%')) and not password:
        return jsonify({'message': 'Неверные учетные данные'}), 401

    # Создаём токен доуступа
    identity = {'audience': audience, 'weekType': week_type}
    expires_delta = timedelta(hours=2)

    access_token = create_access_token(identity=identity, expires_delta=expires_delta)

    return jsonify({'access_token': access_token}), 200
