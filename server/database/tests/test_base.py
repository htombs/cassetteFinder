from flask_testing import TestCase
from server.api import app
from server.database.tables.database import Database
import sqlite3


class BaseTestCase(TestCase):
    def create_test_app(self):
        app.config['TESTING'] = True
        return app
    
    def __init__(self, dbname=':memory:'):
        try:
            self.connection = sqlite3.connect(dbname, check_same_thread=False)
        except:
            print('Error')
        finally:
            pass