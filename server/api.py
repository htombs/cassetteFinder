from flask import Flask, jsonify
from flask_cors import CORS

from .database.tables.database import Database
from .database.tables.cassettes_table import CassettesTable
from .database.tables.distributor_table import DistributorTable

app = Flask(__name__)
# NOTE: This allows any web address to call the API - so we no longer need the 'no-cors' call in the frontend
# We limit this to just the two localhost addresses with their ports for security reasons =]
# 5000 is this API, 8080 is the website / frontend
CORS(app, origins=['http://localhost:5000', 'http://localhost:8080', 'http://127.0.0.1:5000', 'http://127.0.0.1:5500', 'http://127.0.0.1:8080'])
   
def __init__(self, db=Database()):
        self.db = db

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Cassette Finder API"})


@app.route("/__seed")
def seed():
    db = Database()

    distributors = DistributorTable(db=db)
    distributors.create()
    distributors.seed()
    d = distributors.select(f"SELECT * FROM {distributors.table_name}",[])

    cassettes = CassettesTable(db=db)
    cassettes.create()
    c = cassettes.seed()

    return jsonify({"message": "Database seeded"})

@app.route("/speed/<speed>/ratio/<ratio>/brand/<brand>")
def cassettes(speed, ratio, brand):
    print(f"Speed: {speed}")
    print(f"Ratio: {ratio}")
    print(f"Brand: {brand}")

    table = CassettesTable()
    result = table.get_cassettes(speed=speed, ratio=ratio, brand=brand)
    return jsonify(result)

@app.route("/__drop")
def drop():
    db = Database()

    distributors = DistributorTable(db=db)
    distributors.drop()

    cassettes = CassettesTable(db=db)
    cassettes.drop()

    return jsonify({"message": "Database dropped"})


if __name__ == "__main__":
    app.run(debug=True)
