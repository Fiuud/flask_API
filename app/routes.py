from flask import request
from app import app
from app.src import home, qr, student, login
from flask_jwt_extended import jwt_required, get_jwt_identity


# маршрут для главной страницы
@app.route('/')
def index():
    return home.index()


# маршрут для создания нового Студента
@app.route('/student/add', methods=['POST'])
def create_student():
    return student.create_student(request.json)


# маршрут для обработки qr кода студента
@app.route('/qr/validate', methods=['POST'])
@jwt_required()
def qr_validate():
    return qr.qr_validate(request.json)


# маршрут для авторизации сканера и получения токена доступа
@app.route('/login', methods=['POST'])
def scanner_login():
    return login.scanner_login(request.json)

