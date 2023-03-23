import rsa
import time
import datetime
import base64

from flask import jsonify, abort
from flask_jwt_extended import get_jwt_identity

from sqlalchemy import cast, func, JSON, DATE

from models.controllers import StudentController, VisitController
from extensions.database_extension import db_session
from models import Event, Class, Visit


def get_lesson_start_time(current_time: float, decrypted_qr_time: int):
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
        if start_timestamp < decrypted_qr_time < end_timestamp:
            print(start)
            return start
    else:
        return False


# TODO: написать функцию для получения типа недели
def get_week_type():
    ...


def qr_validate(request):
    if not request or 'qr_data' not in request:
        abort(400)
    try:
        google_id, encrypted_qr_time = request["qr_data"].split("|")
        int(google_id)
    except ValueError:
        print(request["qr_data"])
        abort(400)
        return jsonify()
    print(request["qr_data"])
    print(request["qr_data"].split("|"))
    jwt_data = get_jwt_identity()
    audience = jwt_data["audience"]

    current_time = time.time()
    week_type = get_week_type()  # TODO: написать функцию для получения типа недели

    student = StudentController.get_student(student_google_id=google_id)
    private_key = rsa.PrivateKey.load_pkcs1(student.privateKey)
    decrypted_qr_time = int((rsa.decrypt(base64.b64decode(encrypted_qr_time), private_key)).decode())

    qr_weekday = time.strftime('%A', time.localtime(decrypted_qr_time))[:2].upper()

    if not (lesson_start_time := get_lesson_start_time(current_time, decrypted_qr_time)):
        return jsonify({'status': 'failure'})

    event = db_session.query(Event, Class).filter(
        Event.summaryId == Class.id,
        Event.location.like(f'%{audience}%'),
        func.substring(func.json_extract_path_text(cast(Event.start, JSON), 'dateTime'), 12, 5) == lesson_start_time,
        Event.recurrence[1].contains(f'BYDAY={qr_weekday}'),
        func.json_extract_path_text(cast(Event.extendedProperties, JSON), 'shared', 'weekType') == week_type,
        func.json_extract_path_text(cast(Event.extendedProperties, JSON), 'shared', 'weekType') == 'both'
    ).all()

    print(len(event))

    if not event:
        return jsonify({"status": "event not started"})
    else:
        event = event[0]
        print(event[0].id)
    if (current_time - decrypted_qr_time) < 35:
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
