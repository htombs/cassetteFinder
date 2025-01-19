import sqlite3
from .database import Database


class DistributorTable():
    
    def __init__(self, db=Database()):
        self.db = db.connection
        self.table_name = "distributor_table"
    
    def create(self) -> list:
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name} 
            (distributor_id INTEGER PRIMARY KEY, 
            distributor_name VARCHAR(255),
            distributor_link_url VARCHAR(255))'''

        cursor = self.db.cursor()
        rows = cursor.execute(query).fetchall()
        cursor.close()
        return rows

    def seed(self) -> list:
        data = [
            ("Bob Elliot", "https://www.bob-elliot.co.uk/"),
            ("Chicken Cyclekit", "https://www.chickencyclekit.co.uk/"),
            ("Greyville", "https://www.greyville.com/"),
            ("Ison Distribution", "https://www.ison-distribution.com/"),
            ("Mackadams", "https://www.mackadamfactors.co.uk/"),
            ("Madison", "https://www.madisonb2b.co.uk/"),
            ("Upgrade", "https://www.upgradebikes.co.uk/"),
            ("ZyroFisher", "https://www.zyrofisherb2b.co.uk/")
        ]
        cursor = self.db.cursor()
        result = cursor.executemany(f"INSERT INTO {self.table_name} (distributor_name, distributor_link_url) VALUES(?, ?)", data) 

        rows = result.fetchall()
        cursor.close()
        return rows

        
    def select(self, query: str, parameters: list) -> list:
        cursor = self.db.cursor()
        rows = cursor.execute(query, parameters).fetchall()
        cursor.close()
        return rows

    def get_distributor(self, name: str) -> list:
        query = f"SELECT distributor_name, distributor_link_url FROM {self.table_name} WHERE distributor_name = ?"
        parameters = [name]
        return self.select(query, parameters)