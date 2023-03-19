from flask import render_template, request, jsonify
import datetime
import time
from app.extensions import db_session
from app.models import Visit, Event, Class, Student, Teacher
from app.controllers import TeacherController, EventController
import calendar
import locale


def index():
    session_id = 'ed10ccd9-11a1-462b-b7e4-a7374eddf296'  # Получаем при логине преподавателя
    visits = list()

    teacher_name = TeacherController.get_teacher(session_id).name  # Имя преподователя
    teacher_lessons = EventController.get_event(teacher_name=teacher_name)  # Список пар преподователя

    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    calendar_months = list(calendar.month_name)[1:]
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    print(calendar_months)
    if request.args.get('event_id') and request.args.get('date'):
        event_id = request.args.get('event_id')
        date = datetime.datetime.strptime(request.args.get('date'), "%Y-%m-%d")
        # weekday = time.strftime('%A', time.localtime(date.timestamp()))[:2].upper()
        # month_day = datetime.datetime.strftime(date, '%B, %d').replace('0', ' ')

        start_time = datetime.datetime.combine(date, datetime.datetime.min.time())
        end_time = datetime.datetime.combine(date, datetime.datetime.max.time())

        visits = db_session.query(Visit, Student, Event).filter(
            Visit.studentId == Student.id,
            Visit.eventId == event_id,
            Visit.eventId == Event.id,
            Visit.visitTime.between(start_time, end_time)
        ).order_by(Visit.visitTime).all()
    return render_template('index.html', teacher_lessons=teacher_lessons, visits=visits, months=calendar_months)
