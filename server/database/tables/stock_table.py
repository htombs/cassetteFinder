from .database import Database, response


class StockTable():
    def __init__(self, db=Database()):
        self.db = db
        self.table_name = "stock_table"

    def create(self) -> list:
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name}
                    (id INTEGER PRIMARY KEY,
                    part_number VARCHAR(255),
                    stock_status INT,
                    distributor_id INT)
                    '''
        
        return self.db.run(query, [])

    def insert(self, data = []) -> list:
        return self.db.run_many(f"INSERT INTO {self.table_name} (part_number, stock_status, distributor_id) VALUES (?, ?, ?)", data)
    
    def drop(self) -> None:
        return self.db.run(f"DROP TABLE IF EXISTS {self.table_name}", [])