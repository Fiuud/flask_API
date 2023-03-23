from sqlalchemy import Column, VARCHAR
from extensions.database_extension import base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Class(base):
    __tablename__ = 'class'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR, nullable=False)

    def __repr__(self):
        return f'<Class: "{self.name}">'
