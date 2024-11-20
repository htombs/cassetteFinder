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
    result = {}
    for idx, item in enumerate(row):
        if item != "" and idx == 0:
            result["brand"] = item
        if item != "" and idx == 1:
            result["model"] = item
        if item != "" and idx == 2:
            result["part_number"] = item
        if item != "" and idx == 3:
            result["speed"] = item
        if item != "" and idx == 4:
            result["ratio"] = item
        if item != "" and idx == 5:
            result["distributor"] = item
        if item != "" and idx == 6:
            result["rrp"] = item
        if item != "" and idx == 7:
            result["link"] = item

    return result

   # return {"brand": row[0], "model": row[1], "part_number": row[2],"speed": row[3],"ratio": row[4],"distributor": row[5],"rrp": row[6], "link": row[7]}

# This is a wrapper function that takes the default rows list and turns it into 
# a list of dictionaries for easier readability.
def response(rows: list):
    response = []

    for row in rows:
        response.append(row_to_dict(row))

    return response
