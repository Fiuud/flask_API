from datetime import datetime

from app.models import Visit, Student, Event
from app.extensions import db_session
import rsa


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

    @staticmethod
    def update_visit():
        return NotImplemented

    @staticmethod
    def delete_visit():
        return NotImplemented
