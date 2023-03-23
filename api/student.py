from flask import Blueprint, request

from services import student_service

student_route = Blueprint('student_route', __name__)


# маршрут для создания нового Студента
@student_route.route('/student/add', methods=['POST'])
def create_student():
    return student_service.create_student(request.json)
