from unittest.mock import MagicMock
import unittest
import sqlite3
from server.database.tables.database import connect_database, row_to_dict, response
from pathlib import WindowsPath, Path

class MyTests(unittest.TestCase):

    def test_sqlite3_connect_success(self):

        sqlite3.connect = MagicMock(return_value='connection succeeded')

        dbc = connect_database()
        sqlite3.connect.assert_called_with(WindowsPath(f"{Path.cwd()}/server/database/tables/cassette_finder.db")) 
        self.assertEqual(dbc,'connection succeeded')
    
    def test_row_to_dict(self):
        input_list = ["test-brand", "test-model", "test-part_number", "test-speed", "test-ratio", "test-distributor", "test-rrp", "test-link"]
        got = row_to_dict(input_list)
        want = {"brand": "test-brand", "model":"test-model", "part_number":"test-part_number", "speed":"test-speed", "ratio":"test-ratio", "distributor":"test-distributor", "rrp":"test-rrp", "link":"test-link"}
        self.assertEqual(got, want, "it didnt work")

    def test_response(self):
        row1 = (1, "Shimano", "HG400", "CSHG4008145", 8, "11-45", "Madison", 36.99, 6)
        row2 = (2, "Shimano", "HG400", "CSHG4008145", 8, "11-45", "Madison", 36.99, 6)
        row3 = (3, "Shimano", "HG400", "CSHG4008145", 8, "11-45", "Madison", 36.99, 6)
        input_list = [row1, row2, row3]
        got = response(input_list)
        want = [row_to_dict(row1), row_to_dict(row2), row_to_dict(row3)]
        self.assertEqual(got, want, "it didnt work")
