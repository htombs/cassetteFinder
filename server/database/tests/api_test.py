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

    def test_api_route_skus(self):
        stock_table = StockTable(db=self.database)
        stock_table.create()
        stock_table.insert([["CSHG4008145", 0, 6]])
        seed = self.client.get('/__seed')
        self.assertEqual(seed.status_code, 200)
        response = self.client.get('/__skus')
        self.assertEqual(response.status_code, 200)
        print("Actual Response:", response.get_json())

        actual_response = response.get_json()
        # extract only the first sku from the response
        first_response = actual_response[0] if actual_response else None
        expected_response = 'CSHG4008145'
            
        self.assertEqual(first_response, expected_response)

    def test_api_route_stock(self):
        # Create the stock table
        stock_table = StockTable(db=self.database)
        stock_table.create()

        # Define the data to be sent in the POST request
        stock_data = [
            ["CSHG4008145", 0, 6],  # part_number, stock_status, distributor_id
            ["CSLG70011145", 1, 6]
        ]

        # Send a POST request to the /stock endpoint
        response = self.client.post("/stock", json=stock_data)

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Query the stock table to verify the data was inserted
        inserted_data = stock_table.select(f"SELECT * FROM {stock_table.table_name}", [])
        print("Inserted Data:", inserted_data)

        # Define the expected data in the stock table
        expected_data = [
            (1, "CSHG4008145", 0, 6),  # id, part_number, stock_status, distributor_id
            (2, "CSLG70011145", 1, 6)
        ]

        # Assert that the inserted data matches the expected data
        self.assertEqual(inserted_data, expected_data)

if __name__ == '__main__':
    unittest.main()        