import sqlite3
from .database import connect_database

connect = connect_database()
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS distributor_table (distributor_id INT PRIMARY KEY, distributor_name VARCHAR(255))''')

cursor.execute('''REPLACE INTO distributor_table (distributor_id, distributor_name)
               VALUES
               (1, "Bob Elliot"),
               (2, "Chicken Cyclekit"),
               (3, "Greyville"),
               (4, "Ison Distribution"),
               (5, "Mackadams"),
               (6, "Madison"),
               (7, "Upgrade"),
               (8, "ZyroFisher")
               ''')

connect.commit()