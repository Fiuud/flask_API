from flask import request
from app import app
from app.src import home, qr, student


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
def qr_validate():
    return qr.qr_validate(request.json)
