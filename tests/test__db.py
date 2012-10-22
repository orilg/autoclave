from .test_utils import TestCase
from flask_app import app
from flask_app import db

class MongoKitTestCase(TestCase):
    def test__creation(self):
        with app.app.app_context():
            db.db.connect()
            self.assertTrue(db.db.connected)
            s = db.db.SampleDatabaseObject()
            s.save()
