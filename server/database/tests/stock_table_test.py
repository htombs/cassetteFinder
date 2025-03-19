import unittest
from server.database.tables.stock_table import StockTable
from server.database.tables.database import Database

class TestStockTable(unittest.TestCase):
    
    def test_create(self):
        test_database = Database(dbname=":memory")

        stock = StockTable(db=test_database)
        stock.create()

        got = stock.select(f'''SELECT * FROM {stock.table_name}''',[])
        want = []
        self.assertEqual(got, want, f"test failed: got {got}, want {want}")
    
    def test_insert(self):
        test_database = Database(dbname=":memory")

        stock = StockTable(db=test_database)
        stock.create()
        stock.insert()

        got = stock.select(f'''SELECT stock_status FROM {stock.table_name} WHERE stock_status="1" LIMIT 1 ''')
        want = [("1,")]
        self.assertEqual(got, want, f"test failed: got {want}, want {want}")