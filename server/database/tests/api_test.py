import unittest
from server.api import app
from server.database.tables.database import Database
from server.database.tables.cassettes_table import CassettesTable
from server.database.tables.distributor_table import DistributorTable
from server.database.tables.stock_table import StockTable


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
        print("Actual Response:", response.get_json())
        expected_response =  {
            "data": {
                "cassettes": [],
                "distributors": [
                    [1, 'Bob Elliot', 'https://www.bob-elliot.co.uk/'], 
                    [2, 'Chicken Cyclekit', 'https://www.chickencyclekit.co.uk/'], 
                    [3, 'Greyville', 'https://www.greyville.com/'], 
                    [4, 'Ison Distribution', 'https://www.ison-distribution.com/'], 
                    [5, 'Mackadams', 'https://www.mackadamfactors.co.uk/'], 
                    [6, 'Madison', 'https://www.madisonb2b.co.uk/'], 
                    [7, 'Upgrade', 'https://www.upgradebikes.co.uk/'], 
                    [8, 'ZyroFisher', 'https://www.zyrofisherb2b.co.uk/']]}, 
                    "message": "Database seeded"
                }
        self.assertEqual(response.get_json(), expected_response)

    def test_api_route_cassettes(self):
        test_database = Database(dbname = ':memory:')

        cassettes_table = CassettesTable(db=test_database)
        cassettes_table.create()
        cassettes_table.seed()
        
        self.client.get('/__seed')
        response = self.client.get('/speed/8/ratio/12-46/brand/Microshift')
        self.assertEqual(response.status_code, 200)
        print("Actual Response:", response.get_json())

        expected_response = {
            "brand": "Microshift",
            "distributor": "Ison Distribution",
            "link": "https://www.ison-distribution.com/",
            "model": "Acolyte",
            "part_number": "CSMSH8246",
            "ratio": "12-46",
            "rrp": 39.99,
            "speed": 8
        }
    
        self.assertEqual(response.get_json(), expected_response)

    def test_api_route_drop(self):  
        response = self.client.get('/__drop')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Database dropped"})

if __name__ == '__main__':
    unittest.main()