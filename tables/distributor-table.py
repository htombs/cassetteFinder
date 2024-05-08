import sqlite3

connect = sqlite3.connect('cassette_finder.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS distributor (distributor id INT PRIMARY KEY, distributor VARCHAR(255))''')

cursor.execute('''INSERT INTO TABLE distributor (distributor_id, ditributor)
               VALUES
               (1, Bob-Elliot)
               (2, Chicken Cyclekit)
               (3, Greyville)
               (4, Ison Distribution)
               (5, Mackadams)
               (6, Madison)
               (7, Upgrade)
               (8, ZyroFisher)
               ''')