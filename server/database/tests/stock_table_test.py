import unittest
from server.database.tables.stock_table import StockTable
from server.database.tables.database import Database

class TestStockTable(unittest.TestCase):
    
    def test_create(self):
        test_database = Database(dbname=":memory:")

        stock = StockTable(db=test_database)
        stock.create()
        print("Stock Table Contents:", stock.select(f"SELECT * FROM {stock.table_name}", []))

        got = stock.select(f'''SELECT * FROM {stock.table_name}''',[])
        want = []
        self.assertEqual(got, want, f"test failed: got {got}, want {want}")

        
    
    def test_insert(self):
        test_database = Database(dbname=":memory:")

        stock = StockTable(db=test_database)
        stock.create()
        stock_data = [
            ["CSLG70011145", 1, 6]
        ]
        stock.insert(stock_data)

        got = stock.select(f'''SELECT stock_status FROM {stock.table_name} WHERE stock_status="1" LIMIT 1 ''')
        want = [(1,)]
        self.assertEqual(got, want, f"test failed: got {got}, want {want}")