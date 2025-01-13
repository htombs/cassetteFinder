from unittest.mock import MagicMock, Mock, patch
import unittest
import sqlite3
from server.database.tables.cassettes_table import connect_database, createCassettesTable, insertCassettesData
from pathlib import WindowsPath, Path

@patch('server.database.tables.cassettes_table.connect_database')
def connect_test_database(self):
    return sqlite3.connect(WindowsPath(f"{Path.cwd()}/server/database/tables/cassette_finder_test.db"))

class TestCassettesTable(unittest.TestCase):

    def test_sqlite3_connect_success(self):        
        
        sqlite3.connect = MagicMock(return_value='connection succeeded')

        dbc = connect_database()
        sqlite3.connect.assert_called_with(WindowsPath(f"{Path.cwd()}/server/database/tables/cassette_finder.db"))
        self.assertEqual(dbc,'connection succeeded')

    def test_createCassettesTable(self):
        with patch('server.database.tables.cassettes_table.connect_database'):
            sqlite3.connect = MagicMock(return_value='connection succeeded')
            dbc = connect_database()
            dbc.assert_called_with('''CREATE TABLE IF NOT EXISTS cassettes_table
               (id INTEGER PRIMARY KEY,
               brand VARCHAR(255),
               model VARCHAR(255),
               partNumber VARCHAR(255),
               speed INT,
               ratio VARCHAR(10),
               distributor VARCHAR(255),
               rrp DECIMAL(10,2),
               distributor_id INT,
               FOREIGN KEY (distributor_id) REFERENCES distributor_table (distributor_id))''')
            self.assertEqual()


    # def test_createCassettesTable(self):
    #     with patch('server.database.tables.cassettes_table.connect_database'):
    #         sqlite3.connect = MagicMock(return_value=connect_test_database())
    #         mock_cursor = sqlite3.connect.return_value.cursor.return_value
    #         mock_cursor.execute(createCassettesTable())
    #         sqlite3.connect.assert_called_with(WindowsPath(f"{Path.cwd()}/server/database/tables/cassette_finder_test.db"))
    #         self.assertEqual()



    def test_insertCassettesData(self):
        insertCassettesData()


if __name__ == '__main__':
    unittest.main()
    