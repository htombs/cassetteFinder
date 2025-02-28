from flask import Flask, jsonify
from flask_cors import CORS

from database.tables.database import Database
from database.tables.cassettes_table import CassettesTable
from database.tables.distributor_table import DistributorTable

app = Flask(__name__)
# NOTE: This allows any web address to call the API - so we no longer need the 'no-cors' call in the frontend
# We limit this to just the two localhost addresses with their ports for security reasons =]
# 5000 is this API, 8080 is the website / frontend
CORS(app, origins=['http://localhost:5000', 'http://localhost:8080', 'http://127.0.0.1:5000', 'http://127.0.0.1:5500', 'http://127.0.0.1:8080'])

app.config["DATABASE"] = Database()

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Cassette Finder API"})

@app.route("/__seed")
def seed():
    distributors = DistributorTable(db=app.config["DATABASE"])
    distributors.create()
    distributors.seed()
    d = distributors.select(f"SELECT * FROM {distributors.table_name}",[])


    cassettes = CassettesTable(db=app.config["DATABASE"])
    cassettes.create()
    c = cassettes.seed()

    response = {"distributors": d, "cassettes": c}

    return jsonify({"message": "Database seeded", "data": response})

@app.route("/speed/<speed>/ratio/<ratio>/brand/<brand>")
def cassettes(speed, ratio, brand):
    table = CassettesTable(db=app.config["DATABASE"])
    result = table.get_cassettes(speed=speed, ratio=ratio, brand=brand)
    return jsonify(result)

@app.route("/__drop")
def drop():
    distributors = DistributorTable(db=app.config["DATABASE"])
    distributors.drop()

    cassettes = CassettesTable(db=app.config["DATABASE"])
    cassettes.drop()

    return jsonify({"message": "Database dropped"})

if __name__ == "__main__":
    app.run(debug=True)