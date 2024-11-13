from unittest.mock import MagicMock,Mock
import unittest
import sqlite3
from database.tables.database import connect_database, row_to_dict
from pathlib import WindowsPath

class MyTests(unittest.TestCase):

    def test_sqlite3_connect_success(self):

        sqlite3.connect = MagicMock(return_value='connection succeeded')

        dbc = connect_database()
        sqlite3.connect.assert_called_with(WindowsPath('C:/Users/hazto/Documents/Work/cassette.finder/server/database/tables/cassette_finder.db'))
        self.assertEqual(dbc,'connection succeeded')
    
    def test_row_to_dict(self):
        input_list = ["test-brand", "test-model", "test-part_number", "test-speed", "test-ratio", "test-distributor", "test-rrp", "test-link"]
        got = row_to_dict(input_list)
        want = {"brand": "test-brand", "model":"test-model", "part_number":"test-part_number", "speed":"test-speed", "ratio":"test-ratio", "distributor":"test-distributor", "rrp":"test-rrp", "link":"test-link"}
        self.assertEqual(got, want, "it didnt work")

    def test_response(self):
        input_list = []
        # THIS NEEDS TO BE FINISHED, will pick up at later date