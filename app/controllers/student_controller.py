from app.models import Student
from app.extensions import db_session
import rsa


class StudentController:
    @staticmethod
    def get_all_students():
        return db_session.query(Student).all()

    @staticmethod
    def get_student(student_email=None, student_google_id=None):
        if student_email:
            return db_session.query(Student).filter_by(email=student_email).first()
        if student_google_id:
            return db_session.query(Student).filter_by(googleId=student_google_id).first()

    @staticmethod
    def create_student(data: dict[str, str]) -> Student:
        public_key, private_key = rsa.newkeys(1024)
        public_key = public_key.save_pkcs1().decode('utf-8')
        private_key = private_key.save_pkcs1().decode('utf-8')

        student = Student(
            email=data['email'],
            display_name=data['displayName'],
            google_id=data['googleId'],
            public_key=public_key,
            private_key=private_key
        )
        db_session.add(student)
        db_session.commit()
        return student

    @staticmethod
    def update_student(student_email: str, data: dict[str, str]):
        student = db_session.query(Student).filter_by(email=student_email)
        student.email = data['email']
        student.googleId = data['googleId']
        student.displayName = data['displayName']
        return student

    @staticmethod
    def delete_student(student_email):
        db_session.delete(db_session.query(Student).filter_by(email=student_email))
        db_session.commit()
