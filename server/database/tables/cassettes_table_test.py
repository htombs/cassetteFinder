from unittest.mock import MagicMock, Mock, patch
import unittest
import sqlite3
import pdb
from server.database.tables.cassettes_table import CassettesTable
from server.database.tables.distributor_table import DistributorTable
from server.database.tables.database import Database


class TestCassettesTable(unittest.TestCase):

    def test_cassettes_table_create(self):
        test_database = Database(dbname=':memory:')
        cassettes = CassettesTable(db=test_database)
        cassettes.create()

        got = cassettes.select(f'''SELECT * FROM {cassettes.table_name}''',[])
        want = [] # In this case, we have no data, we just want to make sure there's no error
        self.assertEqual(got, want, f"test failed: got {got}, want {want}")


    def test_get_cassette(self):
        test_database = Database(dbname=':memory:')

        distributors = DistributorTable(db=test_database)
        distributors.create()
        distributors.seed()       
        
        cassettes = CassettesTable(db=test_database)
        cassettes.create()
        cassettes.seed()

        speed = "9"
        ratio = "11-34"
        brand = "Tifosi"
        
        got = cassettes.get_cassettes(speed=speed, ratio=ratio, brand=brand)
        want = [{'brand': 'Tifosi', 'model': '9X HG', 'part_number': 'TIF709A', 'speed': 9, 'ratio': '11-34', 'distributor': 'Chicken Cyclekit', 'rrp': 22.99, 'link': 'https://www.chickencyclekit.co.uk/'}] 
        self.assertEqual(got, want, f"test failed: got {got}, want {want}")

if __name__ == '__main__':
    unittest.main()
    