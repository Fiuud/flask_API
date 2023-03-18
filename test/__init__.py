import unittest
from app import app
from app.extensions import db_session


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.config.TestConfig')
        self.app = app.test_client()
        with app.app_context():
            db_session.create_all()

    def tearDown(self):
        with app.app_context():
            db_session.session.remove()
            db_session.drop_all()
