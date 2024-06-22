import sqlite3

connect = sqlite3.connect('cassette_finder.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS distributor_table (distributor_id INT PRIMARY KEY, distributor_name VARCHAR(255))''')

cursor.execute('''INSERT INTO distributor_table (distributor_id, ditributor_name)
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

# def get_table():
#     cursor.execute('''SELECT * FROM db.sqlite_master WHERE type='table';''')

# get_table()