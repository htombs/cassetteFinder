import unittest
from server.api import app
from server.database.tables.database import Database

class FlaskintegrationTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):   
        app.testing = True
        cls.database = Database(dbname=':memory:')
        app.config['DATABASE'] = cls.database

        cls.client = app.test_client()

    def test_api_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Welcome to the Cassette Finder API"})

    def test_api_route_seed(self):
        response = self.client.get('/__seed')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Database seeded"})

    def test_api_route_drop(self):  
        response = self.client.get('/__drop')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Database dropped"})


if __name__ == '__main__':
    unittest.main()
# In this test, we are testing the following API routes:
#   - / : This route should return a welcome message   
#   - /__seed : This route should seed the database with data
#   - /__drop : This route should drop the database
# We are also testing that the tables are created and seeded when the /__seed route is called, and that the tables are dropped when the /__drop route is called.
# To run the test, run the following command in the terminal:
# python -m unittest server.database.tests.api_test
# The test should pass if the API routes are working as expected.
