from extensions.database_extension import db_session
from models import TeacherAuth

from werkzeug.security import check_password_hash


class TeacherAuthController:
    @staticmethod
    def get_all_teacher_auth():
        return db_session.query(TeacherAuth).all()

    @staticmethod
    def get_teacher_auth(email, password=None) -> TeacherAuth:
        teacher_auth = db_session.query(TeacherAuth).filter_by(email=email).first()

        if password:
            return teacher_auth if check_password_hash(teacher_auth.password_hash, password) else False
        else:
            return teacher_auth

    @staticmethod
    def update_teacher_auth(data: dict[str, str]) -> TeacherAuth:
        ...

    @staticmethod
    def create_teacher_auth(data: dict[str, str]):
        teacher_auth = TeacherAuth(
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            middle_name=data['middle_name'],
            last_name=data['last_name'],
        )
        db_session.add(teacher_auth)
        db_session.commit()

    @staticmethod
    def delete_teacher_auth(email, password):
        ...
