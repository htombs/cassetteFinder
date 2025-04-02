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
        stock_table = StockTable(db=self.database)
        stock_table.create()
        stock_table.insert([["CSLG70011145", 1, 6]])
        seed = self.client.get('/__seed')
        self.assertEqual(seed.status_code, 200)
        response = self.client.get('/speed/11/ratio/11-45/brand/Shimano')
        self.assertEqual(response.status_code, 200)
        print("Actual Response:", response.get_json())

        expected_response = [{
            'brand': 'Shimano',
            'distributor': 'Madison',
            'link': 'https://www.madisonb2b.co.uk/', 
            'model': 'LG700',
            'part_number': 'CSLG70011145',
            'ratio': '11-45',
            'rrp': 129.99,
            'speed': 11, 
            'stock_status': 1
            }]
            
    
        self.assertAlmostEqual(response.get_json(), expected_response)

    def test_api_route_drop(self):  
        response = self.client.get('/__drop')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Database dropped"})

if __name__ == '__main__':
    unittest.main()

        # test_database = Database(dbname = ':memory:')

        # cassettes_table = CassettesTable(db=test_database)
        # cassettes_table.create()
        # cassettes_table.seed()

        # distributors_table = DistributorTable(db=test_database)
        # distributors_table.create()
        # distributors_table.seed()

        