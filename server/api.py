from flask import Flask, jsonify
from database.cassette_finder_script import get_brand_8spd, get_brand_9spd, get_brand_10spd, get_brand_11spd, get_brand_8spd_all, get_brand_9spd_all, get_brand_10spd_all, get_brand_11spd_all
from database.cassette_finder_script import get_distributor_8spd, get_distributor_9spd, get_distributor_10spd, get_distributor_11spd, get_distributor_8spd_all, get_distributor_9spd_all, get_distributor_10spd_all, get_distributor_11spd_all
from database.cassette_finder_script import get_speed_8spd, get_speed_9spd, get_speed_10spd, get_speed_11spd, get_speed_8spd_all, get_speed_9spd_all, get_speed_10spd_all, get_speed_11spd_all
from database.cassette_finder_script import get_ratio_8spd, get_ratio_9spd, get_ratio_10spd, get_ratio_11spd, get_ratio_8spd_all, get_ratio_9spd_all, get_ratio_10spd_all, get_ratio_11spd_all

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Cassette Finder API"})

@app.route("/distributor")
def distributor_home():
    return jsonify({"message": "Pick a Distributor"})

@app.route("/distributor/<distributor>")
def distributor_list(distributor):
    print(f"Distributor query: {distributor}")
    return jsonify(get_distributor_8spd(distributor), get_distributor_9spd(distributor), get_distributor_10spd(distributor), get_distributor_11spd(distributor))

@app.route("/brands")
def brand_home():
    return jsonify({"message": "Pick a Brand"})
@app.route("/brands/<brand>")
def brands_list(brand):
    print(f"Brand query: {brand}")
    return jsonify(get_brand_8spd(brand), get_brand_9spd(brand), get_brand_10spd(brand), get_brand_11spd(brand))

# The defaults is what the "ratio" parameter in the function will be set to
# if the user does not add a parameter to the url.
# for example:
#   localhost:5000/ratios will set the "ratio" variable as 11-52
# but
#   localhost:5000/ratios/11-36 will set the "ratio" variable as 11-36


@app.route("/ratio")
def ratio_home():
    return jsonify({"message": "Pick a Ratio"})
@app.route("/ratio/<ratio>")
def ratio_list(ratio):
    print(f"Ratio Query: {ratio}")
    return jsonify(get_ratio_8spd(ratio), get_ratio_9spd(ratio), get_ratio_10spd(ratio), get_ratio_11spd(ratio))


@app.route("/speeds")
def speed_home():
    return jsonify({"message": "Pick a Speed"})
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
