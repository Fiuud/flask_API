from flask import Blueprint, request

from services import student_service

student_route = Blueprint('student', __name__, url_prefix='/student')


# маршрут для создания нового Студента
@student_route.route('/add', methods=['POST'])
def create_student():
    return student_service.create_student(request.json)
