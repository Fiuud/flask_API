import uuid

from sqlalchemy import Column, VARCHAR, ForeignKey, Text, text
from extensions.database_extension import base
from sqlalchemy.dialects.postgresql import UUID

from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class TeacherAuth(base, UserMixin):
    __tablename__ = 'teacherAuth'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    email = Column(VARCHAR(100), nullable=False)
    password_hash = Column(VARCHAR(255), nullable=False)
    first_name = Column(VARCHAR(20), nullable=False)
    middle_name = Column(VARCHAR(20), nullable=False)
    last_name = Column(VARCHAR(20), nullable=False)
    avatar = Column(Text)

    def __init__(self, email, password, first_name, middle_name, last_name):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def __repr__(self):
        return f'<Email: "{self.email}", Teacher: "{self.last_name} {self.first_name[0]}.{self.middle_name[0]}.">'
