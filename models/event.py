from sqlalchemy import Column, VARCHAR, Text, ForeignKey, ARRAY, text
from extensions.database_extension import base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Event(base):
    __tablename__ = 'event'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    location = Column(VARCHAR)
    description = Column(VARCHAR)
    start = Column(Text)
    end = Column(Text)
    recurrence = Column(ARRAY(Text))
    extendedProperties = Column(Text)

    summaryId = Column(UUID(as_uuid=True), ForeignKey("class.id"))

    def __repr__(self):
        return f'<Room: "{self.location.replace(", КИПУ", "")}", ' \
               f'Time: "{self.start[24:29]}", ' \
               f'WeekDay: "{self.recurrence[0][35:37]}">'
