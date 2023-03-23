from datetime import datetime

from models import Visit, Student, Event
from extensions.database_extension import db_session


class VisitController:
    @staticmethod
    def get_all_visits():
        return db_session.query(Visit).all()

    @staticmethod
    def get_visit(student_id):
        return db_session.query(Visit, Student, Event).filter_by(studentId=student_id).all()

    @staticmethod
    def create_visit(student_id: int, visit_time: datetime, event_id: int) -> Visit:
        visit = Visit(student_id, visit_time, event_id)
        db_session.add(visit)
        db_session.commit()
        return visit
