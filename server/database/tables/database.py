import sqlite3


class Database():
    def __init__(self, dbname ='cassette_finder.db'):
        try: 
            self.name = dbname
            self.connection = sqlite3.connect(dbname, check_same_thread=False) 
        except:
            print('Error')
        finally:
            pass
    
    def run(self, query: str, parameters: str) -> list:
        cursor = self.connection.cursor()
        rows = cursor.execute(query, parameters).fetchall()
        self.connection.commit()
        cursor.close()
        return rows
    
    def run_many(self, query: str, parameters: str) -> list:
        cursor = self.connection.cursor()
        rows = cursor.executemany(query, parameters).fetchall()
        self.connection.commit()
        cursor.close()
        return rows

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
        if item != "" and idx == 8:
            result["stock_status"] = item

    return result

# This is a wrapper function that takes the default rows list and turns it into 
# a list of dictionaries for easier readability.
def response(rows: list):
    response = []

    for row in rows:
        response.append(row_to_dict(row))

    return response
