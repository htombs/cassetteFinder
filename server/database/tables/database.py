import sqlite3
from pathlib import Path
THIS_FOLDER = Path(__file__).parent.resolve()
db = THIS_FOLDER / "cassette_finder.db"

def connect_database():
    return sqlite3.connect(db)

# This function turns a row from the db into an object, for easier usage
# NOTE: Notice that the row indexes correlate to the SELECT names from the SQL Query
# except the part number, because we use this as an "index"
def row_to_dict(row: list):
    return {"brand": row[0], "model": row[1], "part_number": row[2],"speed": row[3],"ratio": row[4],"distributor": row[5],"rrp": row[6]}

# This is a wrapper function that takes the default rows list and turns it into 
# a list of dictionaries for easier readability.
def response(rows: list):
    response = []

    for row in rows:
        response.append(row_to_dict(row))

    return response
