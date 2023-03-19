from flask import jsonify
import datetime
import time

from databases.extension import session, Event, Class, Student, TeacherAuth, Teacher, Visit


def test():
    # qr_time = int(time.time())
    # qr_weekday = time.strftime('%A', time.localtime(qr_time))[:2].upper()
    # today = datetime.date.today()
    #
    # pattern_date, pattern_timestamp = '%Y-%m-%d', '%Y-%m-%d %H:%M:%S'
    #
    # time_list = {
    #     '08:00': '09:30',
    #     '09:40': '11:10',
    #     '11:30': '13:00',
    #     '13:10': '14:40',
    #     '14:50': '16:20',
    #     '16:30': '18:00'}
    #
    # lesson_start_time = ''
    #
    # for start, end in time_list.items():
    #     start_timestamp = int(
    #         time.mktime(time.strptime(f"{today.strftime(pattern_date)} {start}:00", pattern_timestamp)))
    #     end_timestamp = int(
    #         time.mktime(time.strptime(f"{today.strftime(pattern_date)} {end}:00", pattern_timestamp)))
    #     if start_timestamp < qr_time < end_timestamp:
    #         lesson_start_time = start
    #
    # query = session.query(Event, Class).filter(Event.summaryId == Class.id, Event.location.contains('236'),
    #                                            Event.start.zcontains(lesson_start_time),
    #                                            Event.recurrence[1].like(f'%BYDAY={qr_weekday}%')).all()
    # for i in query:
    #     print(i[0].recurrence)
    # test_event = [f'{i[0].location.replace(", КИПУ", "")} {i[1].name} {i[0].start}' for i in query]




################################################
    session_id = '13a42b17-34a7-4e07-b278-411f0e670701'
    teacher_name = session.query(Teacher).filter_by(id=session_id).first()
    #
    # # Имея его ID, ищем в -event- дисциплины, которые он ведет (также получаем всю информацию о паре).
    lessons_query = session.query(Event).filter(Event.description.like(f"%{teacher_name.name}%")).all()
    # lessons_id = [i.summaryId for i in lessons_query]
    # events_id = [i.id for i in lessons_query]
    #
    # # Вписываем их в список teacher_lessons (список пар преподавателя на сайте для сортировки):
    # lessons_id = [(session.query(Class).filter(Class.id == lessons_id[i]).first())
    #               for i in range(len(lessons_id))]
    # teacher_lessons = [lessons_id[i].name for i in range(len(lessons_id))]

    # lesson_visits = session.query(Visit, Event).filter(Visit.event_id == events_id).first()
    # print(lesson_visits)

    # lesson_time = [i.start for i in lessons_query]
    # lesson_time = [(i.start.replace(f"{i.start[:24]}", "")).replace(
    #     f'{(i.start.replace(f"{i.start[:24]}", ""))[5:]}', "") for i in lessons_query]
    #
    # print(lesson_time[0])

    # return jsonify(lesson_time)
    return 0

