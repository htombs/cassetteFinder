from flask_testing import TestCase
from server.api import app
from server.database.tables.database import Database
import sqlite3


class BaseTestCase(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.test_database = Database(dbname=':memory:')
        app.config['DATABASE'] = self.test_database
    
    def __init__(self, dbname=':memory:'):
        try:
            self.connection = sqlite3.connect(dbname, check_same_thread=False)
        except:
            print('Error')
        finally:
            pass