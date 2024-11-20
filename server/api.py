from flask import Flask, jsonify
from flask_cors import CORS
from database.cassette_finder_script import get_speed_9spd_all, get_speed_10spd_all, get_speed_11spd_all
from database.cassette_finder_script import get_speed_ratio_9spd , get_speed_ratio_10spd, get_speed_ratio_11spd, get_speed_ratio_brand_8spd

app = Flask(__name__)
# NOTE: This allows any web address to call the API - so we no longer need the 'no-cors' call in the frontend
# We limit this to just the two localhost addresses with their ports for security reasons =]
# 5000 is this API, 8080 is the website / frontend
CORS(app, origins=['http://localhost:5000', 'http://localhost:8080', 'http://127.0.0.1:5000', 'http://127.0.0.1:5500'])

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Cassette Finder API"})

@app.route("/speed/<speed>/ratio/<ratio>/brand/<brand>")
def ratio(speed, ratio, brand):
    print(f"Speed: {speed}")
    print(f"Ratio: {ratio}")
    print(f"Brand: {brand}")

    result = get_speed_ratio_brand_8spd(speed, ratio, brand)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


