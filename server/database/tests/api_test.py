from server.database.tests.test_base import BaseTestCase
from server.database.tables.database import Database
from server.api import app


class api_test(BaseTestCase):
    def test_api_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Welcome to the Cassette Finder API"})

    def test_api_route_seed(self):
        test_database = Database(dbname=':memory:')
        api = app(db=test_database)

        response = api('/__seed')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Database seeded"})

    def test_api_route_drop(self):
        test_database = Database(dbname=':memory:')
        api = app(db=test_database)

        response = api('/__drop')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Database dropped"})