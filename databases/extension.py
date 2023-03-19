from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, VARCHAR, Text, ForeignKey, DateTime, SmallInteger, Boolean, ARRAY, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.orm import sessionmaker
import uuid

import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PSW = os.getenv('PSW')
DB = os.getenv('DB')

db_url = f"postgresql+psycopg2://{USER}:{PSW}@{HOST}/{DB}"
db = create_engine(db_url, echo=False)
base = declarative_base()


class Teacher(base):
    __tablename__ = 'teacher'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(VARCHAR)

    def __repr__(self):
        return f'<ID: "{self.id}", Teacher: "{self.name}">'


class TeacherAuth(base):
    __tablename__ = 'teacherAuth'

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(50))
    password = Column(VARCHAR)

    teacher_id = Column(UUID(as_uuid=True), ForeignKey('teacher.id'))

    def __init__(self, email, password, teacher_id):
        self.email = email
        self.password = password
        self.teacher_id = teacher_id

    def __repr__(self):
        return f'<Email: "{self.email}", TeacherId: "{self.teacher_id}">'


class Visit(base):
    __tablename__ = 'visit'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    visit_time = Column(TIMESTAMP, nullable=False)

    event_id = Column(UUID(as_uuid=True), ForeignKey('event.id'))

    def __init__(self, student_id, visit_time, event_id):
        self.student_id = student_id
        self.visit_time = visit_time
        self.event_id = event_id

    def __repr__(self):
        return f'<StudentID: "{self.student_id}", VisitTime: "{self.visit_time}", Event: "{self.event_id}">'


class Student(base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    email = Column(Text, nullable=False)
    display_name = Column(Text, nullable=False)
    google_id = Column(Text, nullable=False)
    public_key = Column(Text, nullable=False)
    private_key = Column(Text, nullable=False)

    def __init__(self, email, display_name, google_id, public_key, private_key):
        self.email = email
        self.display_name = display_name
        self.google_id = google_id
        self.public_key = public_key
        self.private_key = private_key

    def __repr__(self):
        return f'<Student: "{self.display_name}", Email: "{self.email}">'


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
        return f'<ID "{self.id}" Room: "{self.location}", Time: "{self.start}" - "{self.end}">'


class Class(base):
    __tablename__ = 'class'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR, nullable=False)

    def __repr__(self):
        return f'<Class: "{self.name}">'


Session = sessionmaker(db)
session = Session()
