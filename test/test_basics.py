import unittest
from flask import current_app
from flask_app import create_app, db

class BasicTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('tasting')
        self.app_contex = self.app.app_context()
        self.app_contex.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_contex.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_tasting(self):
        self.assertTrue(current_app.config['TESTING'])




