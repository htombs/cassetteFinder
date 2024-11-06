import sqlite3
from .database import connect_database

connect = connect_database()
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS distributor_table (distributor_id INT PRIMARY KEY, distributor_name VARCHAR(255))''')

# cursor.execute('''ALTER TABLE distributor_table ADD distributor_link_url VARCHAR(255)''')

connect.commit()

cursor.execute('''REPLACE INTO distributor_table (distributor_id, distributor_name, distributor_link_url) 
               VALUES
               (1, "Bob Elliot", "https://www.bob-elliot.co.uk/"),
               (2, "Chicken Cyclekit", "https://www.chickencyclekit.co.uk/"),
               (3, "Greyville", "https://www.greyville.com/"),
               (4, "Ison Distribution", "https://www.ison-distribution.com/"),
               (5, "Mackadams", "https://www.mackadamfactors.co.uk/"),
               (6, "Madison", "https://www.madisonb2b.co.uk/"),
               (7, "Upgrade", "https://www.upgradebikes.co.uk/"),
               (8, "ZyroFisher", "https://www.zyrofisherb2b.co.uk/")
               ''')

connect.commit()