import uuid

from sqlalchemy import Column, Text, UUID, text
from extensions.database_extension import base


class Student(base):
    __tablename__ = 'student'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    email = Column(Text, nullable=False)
    displayName = Column(Text, nullable=False)
    googleId = Column(Text, nullable=False)

    def __init__(self, email, display_name, google_id):
        self.email = email
        self.displayName = display_name
        self.googleId = google_id

    def __repr__(self):
        return f'<Student: "{self.displayName}", ' \
               f'Email: "{self.email}">'
