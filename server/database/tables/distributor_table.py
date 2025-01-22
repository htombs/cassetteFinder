from .database import Database


class DistributorTable():
    
    def __init__(self, db=Database()):
        self.db = db
        self.table_name = "distributor_table"
    
    def create(self) -> list:
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name} 
            (distributor_id INTEGER PRIMARY KEY, 
            distributor_name VARCHAR(255),
            distributor_link_url VARCHAR(255))'''

        return self.db.run(query, [])
    
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
        return self.db.run_many(f"INSERT INTO {self.table_name} (distributor_name, distributor_link_url) VALUES (?, ?)", data)

        
    def select(self, query: str, parameters: list) -> list:
        return self.db.run(query, parameters)

    def get_distributor(self, name: str) -> list:
        query = f"SELECT distributor_name, distributor_link_url FROM {self.table_name} WHERE distributor_name = ?"
        parameters = [name]
        return self.select(query, parameters)
    
    def drop(self) -> None:
        return self.db.run(f"DROP TABLE IF EXISTS {self.table_name}", [])