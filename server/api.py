from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from database.tables.database import Database
from database.tables.cassettes_table import CassettesTable
from database.tables.distributor_table import DistributorTable
from database.tables.stock_table import StockTable



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

    stock = StockTable(db=app.config["DATABASE"])
    stock.create()

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

    stock = StockTable(db=app.config["DATABASE"])
    stock.drop()

    return jsonify({"message": "Database dropped"})

@app.route("/__skus")
def skus():
    table = CassettesTable(db=app.config["DATABASE"])
    result = table.get_skus()
    return jsonify(result)

@app.route("/stock", methods = ['POST'])
def stock():
    data = json.loads(request.get_json())

    table = StockTable(db=app.config["DATABASE"])
    result = table.insert(data)
    return result


if __name__ == "__main__":
    app.run()