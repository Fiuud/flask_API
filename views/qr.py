from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from services import qr_service

qr_route = Blueprint('qr', __name__)


# маршрут для обработки qr кода студента
@qr_route.route('/qr/validate', methods=['POST'])
@jwt_required()
def qr_validate():
    return qr_service.qr_validate(request.json)
