import uuid

from sqlalchemy import Column, VARCHAR, text
from sqlalchemy.dialects.postgresql import UUID
from extensions.database_extension import base


class Teacher(base):
    __tablename__ = 'teacher'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    name = Column(VARCHAR)

    def __repr__(self):
        return f'<ID: "{self.id}", Teacher: "{self.name}">'
