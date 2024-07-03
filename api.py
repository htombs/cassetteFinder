from flask import Flask, request, jsonify
from Database.tables.eight_speed import get_brand_8spd

app = Flask(__name__)

@app.route("/")
def cassettes_list():
    return jsonify(get_brand_8spd("Shimano"))

# cassettes = [
#     { "brand": "shamano",
#      "model": "HG400",
#      "RRP": 36.99}
#      ]

# @app.route("/")
# def get_cassettes():
#     return jsonify(f"{cassettes}".title())

# @app.route('/cassettes/', method=['POST'])
# def add_cassettes():
#     cassettes.append(request.get_json())
#     return '', 204

if __name__ == "__main__":
    app.run(debug=True)