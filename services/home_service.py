from flask import render_template, request
from flask_login import current_user
from extensions.database_extension import db_session
from models import Visit, Event, Student, Teacher
from models.controllers import EventController
from utils import turbo
import datetime


def index():
    teacher_ids = db_session.query(Teacher).filter(
        Teacher.name.like(f'%{current_user.last_name} {current_user.first_name[0]}.{current_user.middle_name[0]}%')
    ).all()  # Получаем все id преподавателя сущности teacher
    visits = list()

    teacher_lessons = []
    for i in teacher_ids:
        teacher_lessons += EventController.get_event(teacher_name=i.name)  # Список пар преподователя
    print(teacher_lessons)

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
    return render_template('index.html', teacher_lessons=teacher_lessons, visits=visits, months=calendar_months,
                           user=current_user)
