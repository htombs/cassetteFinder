from flask import Flask, jsonify
from flask_cors import CORS
from server.database.tables.cassettesTable import get_spd
# from database.tables.nine_speed import get_9spd
# from database.tables.ten_speed import get_10spd
# from database.tables.eleven_speed import get_11spd

app = Flask(__name__)
# NOTE: This allows any web address to call the API - so we no longer need the 'no-cors' call in the frontend
# We limit this to just the two localhost addresses with their ports for security reasons =]
# 5000 is this API, 8080 is the website / frontend
CORS(app, origins=['http://localhost:5000', 'http://localhost:8080', 'http://127.0.0.1:5000', 'http://127.0.0.1:5500', 'http://127.0.0.1:8080'])

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Cassette Finder API"})

@app.route("/speed/<speed>/ratio/<ratio>/brand/<brand>")
def ratio(speed, ratio, brand):
    print(f"Speed: {speed}")
    print(f"Ratio: {ratio}")
    print(f"Brand: {brand}")

    spd = get_spd(speed, ratio, brand)
    # spd9 = get_9spd(speed, ratio, brand)
    # spd10 = get_10spd(speed, ratio, brand)
    # spd11 = get_11spd(speed, ratio, brand)

    result = spd

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
