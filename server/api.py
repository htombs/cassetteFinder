from flask import Flask, jsonify
from database.cassette_finder_script import get_brand_8spd, get_brand_9spd, get_brand_10spd, get_brand_11spd, get_brand_8spd_all, get_brand_9spd_all, get_brand_10spd_all, get_brand_11spd_all
# from database.cassette_finder_script import get_distributor_8spd, get_distributor_9spd, get_distributor_10spd, get_distributor_11spd
# from database.cassette_finder_script import get_speed_8spd, get_speed_9spd, get_speed_10spd, get_speed_11spd
# from database.cassette_finder_script import get_ratio_8spd, get_ratio_9spd, get_ratio_10spd, get_ratio_11spd
from database.cassette_finder_script import get_brands_all

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

@app.route("/brands")
def brand_home():
    return jsonify({"Message": "Pick a brand"})
@app.route("/brands/<brand>")
def brands_list(brand):
    print(f"Brand query: {brand}")
    return jsonify(get_brands_all(brand))

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


@app.route("/speeds")
def speed_home():
    return jsonify({"message": "Choose a speed"})
@app.route("/speeds/<speed>")
def speeds(speed):
    if speed == '8':
        return jsonify(get_brand_8spd_all("*"))
    elif speed == '9':
        return jsonify(get_brand_9spd_all("*"))
    elif speed == '10':
        return jsonify(get_brand_10spd_all("*"))
    elif speed == '11':
        return jsonify(get_brand_11spd_all("*"))
    else:
        return jsonify({"message: no more speeds bro"})

if __name__ == "__main__":
    app.run(debug=True)
