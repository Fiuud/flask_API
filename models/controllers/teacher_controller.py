from models import Teacher
from extensions.database_extension import db_session
import rsa


class TeacherController:
    @staticmethod
    def get_all_teacher():
        return db_session.query(Teacher).all()

    @staticmethod
    def get_teacher(teacher_id) -> Teacher:
        return db_session.query(Teacher).filter_by(id=teacher_id).first()
