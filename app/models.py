from sqlalchemy import (Column, Integer, VARCHAR, Text, ForeignKey, DateTime, SmallInteger, Boolean, ARRAY)
from app.extensions import base
from sqlalchemy.dialects.postgresql import UUID, JSON
import uuid


class Visit(base):
    __tablename__ = 'visit'

    id = Column(Integer, primary_key=True)
    studentId = Column(Integer, ForeignKey('student.id'))
    visitTime = Column(Integer, nullable=False)

    eventId = Column(UUID(as_uuid=True), ForeignKey('event.id'))

    def __init__(self, student_id, visit_time, event_id):
        self.studentId = student_id
        self.visitTime = visit_time
        self.eventId = event_id

    def __repr__(self):
        return f'<StudentID: "{self.studentId}", VisitTime: "{self.visitIime}", Event: "{self.eventId}">'


class Student(base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    email = Column(Text, nullable=False)
    displayName = Column(Text, nullable=False)
    googleId = Column(Text, nullable=False)
    publicKey = Column(Text, nullable=False)
    privateKey = Column(Text, nullable=False)

    def __init__(self, email, display_name, google_id, public_key, private_key):
        self.email = email
        self.displayName = display_name
        self.googleId = google_id
        self.publicKey = public_key
        self.privateKey = private_key

    def __repr__(self):
        return f'<Student: "{self.displayName}", Email: "{self.email}">'


class Event(base):
    __tablename__ = 'event'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location = Column(VARCHAR)
    description = Column(VARCHAR)
    start = Column(Text)
    end = Column(Text)
    recurrence = Column(ARRAY(Text))

    summaryId = Column(UUID(as_uuid=True), ForeignKey("class.id"))

    def __repr__(self):
        return f'<Room: "{self.location}", Time: "{self.start}" - "{self.end}">'


class Class(base):
    __tablename__ = 'class'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR, nullable=False)

    def __repr__(self):
        return f'<Class: "{self.name}">'
