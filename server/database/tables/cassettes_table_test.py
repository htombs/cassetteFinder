from unittest.mock import MagicMock, Mock, patch
import unittest
import sqlite3
from server.database.tables.cassettes_table import connect_database, createCassettesTable, insertCassettesData, get_spd
from pathlib import WindowsPath, Path

@patch('server.database.tables.cassettes_table.connect_database')
def connect_test_database(self):
    return sqlite3.connect(':memory:')

class TestCassettesTable(unittest.TestCase):

    def test_sqlite3_connect_success(self):        
        
        sqlite3.connect = MagicMock(return_value='connection succeeded')

        conn = connect_database()
        sqlite3.connect.assert_called_with(WindowsPath(f"{Path.cwd()}/server/database/tables/cassette_finder.db"))
        self.assertEqual(conn,'connection succeeded')

    def test_createCassettesTable(self):
        with patch('server.database.tables.cassettes_table.connect_database'):
            conn = sqlite3.connect(WindowsPath(f"{Path.cwd()}/server/database/tables/cassette_finder_test.db"))
            cursor = conn.cursor()
            createCassettesTable()
            insertCassettesData()
            sqlSelect = '''SELECT * FROM cassettes_table'''
            sql = cursor.execute(sqlSelect)
            speed = []
            conn.commit()
            rows = sql.fetchall()
            self.assertEqual(speed, rows, "it didn't work")


    def test_get_spd(self):
        speed = "10"
        ratio = "11-42"
        brand = "shimano"
        result = f"{speed}" + f"{ratio}" + f"{brand}"
        # input_list = [speed, ratio, brand]
        got = '''SELECT * FROM cassettes_table WHERE speed = 10 AND ratio = 11-42 AND brand = shimano'''
        want = result
        self.assertEqual(got, want, "it didnt work")

if __name__ == '__main__':
    unittest.main()
    