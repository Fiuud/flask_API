from flask import render_template, request
from app.extensions import db_session
from app.models import Visit, Event, Student
from app.controllers import TeacherController, EventController
from app import turbo
import datetime


def index():
    session_id = 'ed10ccd9-11a1-462b-b7e4-a7374eddf296'  # Получаем при логине преподавателя
    visits = list()

    teacher_name = TeacherController.get_teacher(session_id).name  # Имя преподователя
    teacher_lessons = EventController.get_event(teacher_name=teacher_name)  # Список пар преподователя

    calendar_months = [
        'Январь', 'Февраль', 'Март',
        'Апрель', 'Май', 'Июнь',
        'Июль', 'Август', 'Сентябрь',
        'Октябрь', 'Ноябрь', 'Декабрь'
    ]

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
        if turbo.can_stream():  # обновления {%include ___ %} блоков кода без перезагрузки страницы
            return turbo.stream([
                turbo.update(
                    render_template('_sorting.html', visits=visits), target='sorting_status'),
                turbo.update(
                    render_template('_table.html', visits=visits), target='sorting_table')
            ])
    return render_template('index.html', teacher_lessons=teacher_lessons, visits=visits, months=calendar_months)
