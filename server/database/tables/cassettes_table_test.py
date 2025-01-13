from unittest.mock import MagicMock, Mock, patch
import unittest
import sqlite3
from server.database.tables.cassettes_table import connect_database, createCassettesTable, insertCassettesData
from pathlib import WindowsPath, Path

@patch('server.database.tables.cassettes_table.connect_database')
def connect_test_database(self):
    return sqlite3.connect(WindowsPath(f"{Path.cwd()}/server/database/tables/cassette_finder_test.db"))

class TestCreateCassettesTable(unittest.TestCase):

    def test_sqlite3_connect_success(self):        
        
        sqlite3.connect = MagicMock(return_value='connection succeeded')

        dbc = connect_database()
        sqlite3.connect.assert_called_with(WindowsPath(f"{Path.cwd()}/server/database/tables/cassette_finder.db"))
        self.assertEqual(dbc,'connection succeeded')


    def test_createCassettesTable(self):
        with patch('server.database.tables.cassettes_table.connect_database'):
            sqlite3.connect = MagicMock(return_value=connect_test_database())
            createCassettesTable()
            sqlite3.connect.assert_called_with(WindowsPath(f"{Path.cwd()}/server/database/tables/cassette_finder_test.db"))



    def test_insertCassettesData(self):
        insertCassettesData()


if __name__ == '__main__':
    unittest.main()
    