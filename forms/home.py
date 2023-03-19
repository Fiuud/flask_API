from flask import render_template, request
import datetime
import time
from databases.extension import session, Visit, Event, Class, Student, Teacher


def index():
    session_id = '13a42b17-34a7-4e07-b278-411f0e670701'  # Получаем при логине преподавателя
    sorting = dict()

    # Предметы будут отсеиваться исходя из того, какой преподаватель зашел в систему;
    teacher_name = session.query(Teacher).filter_by(id=session_id).first()

    # Имея его ID, ищем в -event- дисциплины, которые он ведет (также получаем всю информацию о паре).
    lessons_query = session.query(Event).filter(Event.description.like(f"%{teacher_name.name}%")).all()
    events_id = [i.id for i in lessons_query]  # список ID ивентов преподавателя
    lessons_id = [i.summaryId for i in lessons_query]  # список summaryId пар преподавателя в -event-

    # Список ВРЕМЕНИ начала (start) пар перподавателя в -event-
    # lesson_time = [i.start for i in lessons_query]
    lesson_time = [(i.start.replace(f"{i.start[:24]}", "")).replace(
        f'{(i.start.replace(f"{i.start[:24]}", ""))[5:]}', "") for i in lessons_query]

    # Вписываем дисциплины в список lessons_title (список пар преподавателя для сортировки):
    lessons_title = [session.query(Class).filter(Class.id == lessons_id[i]).first()
                     for i in range(len(lessons_id))]
    # список НАЗВАНИЙ пар данного преподавателя:
    lessons_title = [lessons_title[i].name for i in range(len(lessons_title))]
    print(lessons_title)

    index_list = 1  # Индекс для сортировки с парой (изначально выбрана 1-ая пара из списка)
    '24072363-6222-4bf9-acba-bbdd57aa1bbe ------- Разработка сервер.'
    # Имея ДАТУ, ВРЕМЯ НАЧАЛА и НАЗВАНИЕ ПРЕДМЕТА можем получить список присутствоваших на паре:

    # lesson_visits = session.query(Visit, Event).filter(Visit.event_id == teacher_lessons.id).first()
    # choosed_lesson = session.query(Event, Class).filter(Event.summaryId == Class.id,
    #                                                     Event.start.contains(lesson_start_time),
    #                                                     Event.recurrence[1].like(f'%BYDAY={qr_weekday}%')).all()

    display_name = []  # Список имен студентов
    visit_time = []  # Список времен сканирования студента
    if request.args.get('lesson') and request.args.get('date'):
        index_list = int(request.args.get('lesson'))  # Индекс выбранной пары в сортировке
        date = request.args.get('date')
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        weekday = time.strftime('%A', time.localtime(date.timestamp()))[:2].upper()

        date = datetime.datetime.strftime(date, '%B, %d').replace('0', ' ')  # вид для верстки

        sorting = {'lesson': lessons_title,
                   'date_form': request.args.get('date'),
                   'time': lesson_time[index_list - 1],
                   'date': date}

        # Все присутствущие студенты данной пары:
        visits = session.query(Visit).filter(Visit.event_id == events_id[index_list - 1],
                                             Event.recurrence[1].like(f"%BYDAY={weekday}%"),
                                             Visit.visit_time == date).all()

        # Список имен этих студентов:
        visits = [[i.student_id, i.event_id, i.visit_time] for i in visits]
        print(visits)
        # Список времени их сканирования
        visit_time = [visit_time.append(datetime.datetime.fromtimestamp(visits[i][2]).strftime('%H:%M')) for i in range(len(visits))]
        for i in range(len(visits)):
            visit_student = session.query(Student).filter(Student.id == visits[i][0]).all()
            display_name.append(visit_student[0].display_name)
        print(display_name)
        print(visit_time)

    return render_template('index.html', lessons_title=lessons_title, index_list=index_list,
                           lesson_time=lesson_time, sorting=sorting, display_name=display_name,
                           visit_time=visit_time)
