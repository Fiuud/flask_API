from sqlalchemy import Column, Integer, Text
from extensions.database_extension import base


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
        return f'<Student: "{self.displayName}", ' \
               f'Email: "{self.email}">'
