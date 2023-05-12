import rsa
import time
import datetime
import base64

from flask import jsonify, abort
from flask_jwt_extended import get_jwt_identity
from rsa import DecryptionError

from sqlalchemy import cast, func, JSON, DATE

from config import Config
from models.controllers import StudentController, VisitController
from extensions.database_extension import db_session
from models import Event, Class, Visit


def get_lesson_start_time(current_time: float):
    today = datetime.datetime.fromtimestamp(current_time)
    pattern_date, pattern_timestamp = '%Y-%m-%d', '%Y-%m-%d %H:%M:%S'
    time_list = {
        '08:00': '09:30',
        '09:40': '11:10',
        '11:30': '13:00',
        '13:10': '14:40',
        '14:50': '16:20',
        '16:30': '18:00'
    }
    for start, end in time_list.items():
        start_timestamp = int(
            time.mktime(time.strptime(f"{today.strftime(pattern_date)} {start}:00", pattern_timestamp)))
        end_timestamp = int(
            time.mktime(time.strptime(f"{today.strftime(pattern_date)} {end}:00", pattern_timestamp)))
        if start_timestamp < current_time < end_timestamp:
            print(start)
            return start
    else:
        return False


def get_week_type(current_time):
    current_time = datetime.datetime.fromtimestamp(current_time)

    d = datetime.date(current_time.year - 1, 9, 1)

    days_to_monday = (7 - d.weekday()) % 7
    last_september = d + datetime.timedelta(days=days_to_monday)

    cur_date = datetime.datetime.now().date()

    days_since_last_september = (cur_date - last_september).days

    if (days_since_last_september // 7) % 2 != 0:
        return 'numerator'  # "числитель"
    else:
        return 'denominator'  # "знаменатель"


def qr_validate(request):
    if not request or 'qr_data' not in request:
        abort(400)
    try:
        qr_data = rsa.decrypt(base64.b64decode(request["qr_data"]), Config.PRIVATE_KEY).decode().split('|')
    except Exception as e:
        return jsonify({'message': 'incorrect qr-code'})

    google_id, check_in_time = qr_data[0], int(qr_data[1])
    current_time = time.time()

    if not (lesson_start_time := get_lesson_start_time(current_time)):
        return jsonify({'status': 'failure'})

    jwt_data = get_jwt_identity()
    audience = jwt_data["audience"]

    student = StudentController.get_student(student_google_id=google_id)

    qr_weekday = time.strftime('%A', time.localtime(check_in_time))[:2].upper()

    week_type = get_week_type(current_time)
    event = db_session.query(Event, Class).filter(
        Event.summaryId == Class.id,
        Event.location == f'{audience}, КИПУ',
        func.substring(func.json_extract_path_text(cast(Event.start, JSON), 'dateTime'), 12, 5) == lesson_start_time,
        Event.recurrence[1].contains(f'BYDAY={qr_weekday}'),
        (func.json_extract_path_text(cast(Event.extendedProperties, JSON), 'shared', 'weekType') == week_type) |
        (func.json_extract_path_text(cast(Event.extendedProperties, JSON), 'shared', 'weekType') == 'both')
    ).all()

    print(len(event))

    if not event:
        return jsonify({"status": "event not started"})
    else:
        event = event[0]
        print(event[0].id)

    if (current_time - check_in_time) < 35:
        visit_time = datetime.datetime.fromtimestamp(current_time)

        in_visit_list = db_session.query(Visit).filter(
            Visit.studentId == student.id,
            Visit.eventId == event[0].id,
            cast(Visit.visitTime, DATE) == visit_time.date()
        ).first()
        if not in_visit_list:
            VisitController.create_visit(student.id, visit_time, event[0].id)
            return jsonify({"status": "created"}), 201
        return jsonify({"status": "already in list"})
    return jsonify({"status": "expired time"})
