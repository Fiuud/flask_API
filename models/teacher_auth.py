from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from extensions.database_extension import base
from sqlalchemy.dialects.postgresql import UUID


class TeacherAuth(base):
    __tablename__ = 'teacherAuth'

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(50))
    password = Column(VARCHAR(250))

    teacher_id = Column(UUID(as_uuid=True), ForeignKey('teacher.id'))

    def __init__(self, email, password, teacher_id):
        self.email = email
        self.password = password
        self.teacher_id = teacher_id

    def __repr__(self):
        return f'<Email: "{self.email}", TeacherId: "{self.teacher_id}">'

