from flask import Flask, jsonify
from database.tables.eight_speed import get_brand_8spd

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Cassette Finder API"})


# The defaults is what the "brand" parameter in the function will be set to
# if the user does not add a parameter to the url.
# for example:
#   localhost:5000/brands will set the "brand" variable as "Shimano"
# but
#   localhost:5000/brands/Madison will set the "brand" variable as "Madison"

@app.route("/brands", defaults={'brand': "Shimano"})
@app.route("/brands/<brand>")
def brands_list(brand):
    print(f"Brand query: {brand}")
    return jsonify(get_brand_8spd(brand))

# The defaults is what the "ratio" parameter in the function will be set to
# if the user does not add a parameter to the url.
# for example:
#   localhost:5000/ratios will set the "ratio" variable as 11-52
# but
#   localhost:5000/ratios/11-36 will set the "ratio" variable as 11-36


@app.route("/ratios", defaults={'ratio': '11-52'})
@app.route("/ratios/<ratio>")
def ratio_list(ratio):
    print(f"Ratio Query: {ratio}")
    return jsonify(["11-36", "11-48", "11-52"])


@app.route("/speeds", defaults={'speed': '10'})
@app.route("/speeds/<speed>")
def speeds(speed):
    if speed == '8':
        return jsonify(get_brand_8spd("Shimano"))
    elif speed == '9':
        return jsonify(get_brand_9spd("Shimano"))
    elif speed == '10':
        return jsonify(get_brand_10spd("Shimano"))
    elif speed == '11':
        return jsonify(get_brand_11spd("Shimano"))
    else:
        return jsonify({message: "no more speeds bro"})

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
