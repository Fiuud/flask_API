from app.models import Teacher
from app.extensions import db_session
import rsa


class TeacherController:
    @staticmethod
    def get_all_teacher():
        return db_session.query(Teacher).all()

    @staticmethod
    def get_teacher(teacher_id) -> Teacher:
        return db_session.query(Teacher).filter_by(id=teacher_id).first()

    @staticmethod
    def create_teacher(data: dict[str, str]) -> Teacher:
        return NotImplemented

    @staticmethod
    def update_student(student_email: str, data: dict[str, str]):
        return NotImplemented

    @staticmethod
    def delete_student(student_email):
        return NotImplemented
