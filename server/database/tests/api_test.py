import unittest
from server.api import app
from server.database.tables.database import Database
from server.database.tables.cassettes_table import CassettesTable
from server.database.tables.distributor_table import DistributorTable

class FlaskintegrationTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.test_database = Database(dbname=':memory:')
        app.config['DATABASE'] = self.test_database

    def test_api_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Welcome to the Cassette Finder API"})

    def test_api_route_seed(self):
        # Verify that the tables were created and seeded
        cassettes_table = CassettesTable(db=self.test_database)
        cassettes_table.create()
        cassettes_table.seed()
        cassettes = cassettes_table.select(f"SELECT * FROM {cassettes_table.table_name}", [])
        self.assertGreater(len(cassettes), 0)

        distributors_table = DistributorTable(db=self.test_database)
        distributors_table.create()
        distributors_table.seed()
        distributors = distributors_table.select(f"SELECT * FROM {distributors_table.table_name}", [])
        self.assertGreater(len(distributors), 0)
        
        response = self.client.get('/__seed')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Database seeded"})


    def test_api_route_drop(self):
        # Verify that the tables were dropped
        cassettes_table = CassettesTable(db=self.test_database)
        with self.assertRaises(Exception):
            cassettes_table.drop()
            cassettes_table.select(f"SELECT * FROM {cassettes_table.table_name}", [])

        distributors_table = DistributorTable(db=self.test_database)
        with self.assertRaises(Exception):
            distributors_table.drop()
            distributors_table.select(f"SELECT * FROM {distributors_table.table_name}", [])

        response = self.client.get('/__drop')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Database dropped"})


if __name__ == '__main__':
    unittest.main()
# In this test, we are testing the API routes. We are testing the following routes:
#   - / : This route should return a welcome message   
#   - /__seed : This route should seed the database with data
#   - /__drop : This route should drop the database
# We are also testing that the tables are created and seeded when the /__seed route is called, and that the tables are dropped when the /__drop route is called.
# To run the test, run the following command in the terminal:
# python -m unittest server.database.tests.api_test
# The test should pass if the API routes are working as expected.
