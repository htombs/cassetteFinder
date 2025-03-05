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

    def test_api_route_cassettes(self):
        response = self.client.get('/speed/8/ratio/12-46/brand/Microshift')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "brand": "Microshift",
            "distributor": "Ison Distribution",
            "link": "https://www.ison-distribution.com/",
            "model": "Acolyte",
            "part_number": "CSMSH8246",
            "ratio": "12-46",
            "rrp": 39.99,
            "speed": 8})

    def test_api_route_drop(self):  
        response = self.client.get('/__drop')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Database dropped"})

if __name__ == '__main__':
    unittest.main()