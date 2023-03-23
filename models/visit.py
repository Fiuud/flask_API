from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from extensions.database_extension import base
from sqlalchemy.dialects.postgresql import UUID


class Visit(base):
    __tablename__ = 'visit'

    id = Column(Integer, primary_key=True)
    visitTime = Column(TIMESTAMP, nullable=False)

    studentId = Column(Integer, ForeignKey('student.id'))
    eventId = Column(UUID(as_uuid=True), ForeignKey('event.id'))

    def __init__(self, student_id, visit_time, event_id):
        self.studentId = student_id
        self.visitTime = visit_time
        self.eventId = event_id

    def __repr__(self):
        return f'<StudentID: "{self.studentId}", ' \
               f'VisitTime: "{self.visitTime}",' \
               f' Event: "{self.eventId}">'
