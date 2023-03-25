import uuid

from sqlalchemy import Column, ForeignKey, TIMESTAMP, text
from extensions.database_extension import base
from sqlalchemy.dialects.postgresql import UUID


class Visit(base):
    __tablename__ = 'visit'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))

    studentId = Column(UUID(as_uuid=True), ForeignKey('student.id'), nullable=False)
    eventId = Column(UUID(as_uuid=True), ForeignKey('event.id'), nullable=False)
    visitTime = Column(TIMESTAMP, nullable=False)

    def __init__(self, student_id, visit_time, event_id):
        self.studentId = student_id
        self.visitTime = visit_time
        self.eventId = event_id

    def __repr__(self):
        return f'<StudentID: "{self.studentId}", ' \
               f'VisitTime: "{self.visitTime}",' \
               f'Event: "{self.eventId}">'
