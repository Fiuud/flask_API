from flask import request, jsonify, abort
import datetime
import base64
import time
import rsa
from databases.extension import session, Student, VisitList, Event, Class


# Запись присутствия студента
def check():
    if not request.json \
            or not ('qr_data' in request.json) \
            or not ('lecture_room' in request.json):
        abort(400)

    qr_data = request.json["qr_data"]
    lecture_room = request.json["lecture_room"]

    google_id = qr_data[:qr_data.find("|")]
    encrypted_qr_time = base64.b64decode(qr_data[qr_data.find("|") + 1:])

    student = session.query(Student).filter_by(google_id=google_id).first()
    private_key = rsa.PrivateKey.load_pkcs1(student.private_key)

    decrypted_qr_time = int((rsa.decrypt(encrypted_qr_time, private_key)).decode())
    current_time = time.time()
    qr_weekday = time.strftime('%A', time.localtime(decrypted_qr_time))[:2].upper()
    today = datetime.datetime.fromtimestamp(current_time)

    pattern_date, pattern_timestamp = '%Y-%m-%d', '%Y-%m-%d %H:%M:%S'
    time_list = {
        '08:00': '09:30',
        '09:40': '11:10',
        '11:30': '13:00',
        '13:10': '14:40',
        '14:50': '16:20',
        '16:30': '18:00'}

    lesson_start_time = ''
    for start, end in time_list.items():
        start_timestamp = int(
            time.mktime(time.strptime(f"{today.strftime(pattern_date)} {start}:00", pattern_timestamp)))
        end_timestamp = int(
            time.mktime(time.strptime(f"{today.strftime(pattern_date)} {end}:00", pattern_timestamp)))
        if start_timestamp < decrypted_qr_time < end_timestamp:
            lesson_start_time = start
            print(lesson_start_time)
            break
        else:
            return jsonify({"status": "failure"})

    event = session.query(Event, Class).filter(Event.summaryId == Class.id, Event.location.contains(lecture_room),
                                               Event.start.contains(lesson_start_time),
                                               Event.recurrence[1].like(f'%BYDAY={qr_weekday}%')).first()
    # fisrt() для имитации того, что отмечаемся на единственной паре (по разделению на чис. и знам.)

    if (current_time - decrypted_qr_time) < 35:
        visit_time = int(current_time)
        in_visit_list = session.query(VisitList).filter_by(student_id=student.id).all()
        if in_visit_list:
            in_visit_list = in_visit_list[0] if len(in_visit_list) == 1 else in_visit_list[-1]
            if (current_time - in_visit_list.visit_time) > 30:
                add_in_list = VisitList(student.id, visit_time, event[0].id)
                session.add(add_in_list)
                session.commit()
                status = "success"
            else:
                status = "neutral"

        else:
            add_in_list = VisitList(student.id, visit_time, event[0].id)
            session.add(add_in_list)
            session.commit()
            status = "success"
    else:
        status = "failure"

    return jsonify({'status': status})
