from flask import Flask, jsonify
from flask_cors import CORS
from database.cassette_finder_script import get_brand_8spd, get_brand_9spd, get_brand_10spd, get_brand_11spd, get_brand_8spd_all, get_brand_9spd_all, get_brand_10spd_all, get_brand_11spd_all
from database.cassette_finder_script import get_distributor_8spd, get_distributor_9spd, get_distributor_10spd, get_distributor_11spd, get_distributor_8spd_all, get_distributor_9spd_all, get_distributor_10spd_all, get_distributor_11spd_all
from database.cassette_finder_script import get_speed_8spd, get_speed_9spd, get_speed_10spd, get_speed_11spd, get_speed_8spd_all, get_speed_9spd_all, get_speed_10spd_all, get_speed_11spd_all
from database.cassette_finder_script import get_ratio_8spd, get_ratio_9spd, get_ratio_10spd, get_ratio_11spd, get_ratio_8spd_all, get_ratio_9spd_all, get_ratio_10spd_all, get_ratio_11spd_all
from database.cassette_finder_script import get_speed_ratio_8spd, get_speed_ratio_9spd , get_speed_ratio_10spd, get_speed_ratio_11spd

app = Flask(__name__)
# NOTE: This allows any web address to call the API - so we no longer need the 'no-cors' call in the frontend
# We limit this to just the two localhost addresses with their ports for security reasons =]
# 5000 is this API, 8080 is the website / frontend
CORS(app, origins=['http://localhost:5000', 'http://localhost:8080'])


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

# THIS NEEDS FIXING!!! ALL OTHERS NEED FUNCTIONS FOR WHEN THE "ANY" OPTION IS SELECTED
# @app.route("/distributor/any")
# def distributor_any(distributor):
#     print(f"Distributor Query: {distributor}")
#     return jsonify(get_distributor_8spd_all(distributor), get_distributor_9spd_all(distributor), get_distributor_10spd_all(distributor), get_distributor_11spd_all(distributor))

@app.route("/brands")
def brand_home():
    return jsonify({"message": "Pick a Brand"})

@app.route("/brands/<brand>")
def brands_list(brand):
    print(f"Brand query: {brand}")
    return jsonify(get_brand_8spd(brand), get_brand_9spd(brand), get_brand_10spd(brand), get_brand_11spd(brand))

@app.route("/ratio")
def ratio_home():
    return jsonify({"message": "Pick a Ratio"})

@app.route("/ratio/<ratio>")
def ratio_list(ratio):
    print(f"Ratio Query: {ratio}")
    return jsonify(get_ratio_8spd(ratio), get_ratio_9spd(ratio), get_ratio_10spd(ratio), get_ratio_11spd(ratio))

@app.route("/speed")
def speed_home():
    return jsonify({"message": "Pick a Speed"})

@app.route("/speed/<speed>")
def speed_list(speed):
    print(f"Speed Query: {speed}")
    return jsonify(get_speed_8spd(speed), get_speed_9spd(speed), get_speed_10spd(speed), get_speed_11spd(speed))

# This is the route used by the form.

@app.route("/speed/<speed>/ratio/<ratio>")
def ratio(speed, ratio):
    print(f"Speed: {speed}")
    print(f"Ratio: {ratio}")

    # NOTE: There's some special bits of logic we need to do to handle 
    # the "all" queries. 
    if speed == 'all':
        print("fetching all speeds")
        spd_8 = get_speed_8spd_all()
        spd_9 = get_speed_9spd_all()
        spd_10 = get_speed_10spd_all()
        spd_11 = get_speed_11spd_all()

        # add all the results from all the speed calls into one big list
        speeds = spd_8 + spd_9 + spd_10 + spd_11

        # prepare our response list
        response = []

        # If the ratio isn't "all" then we need to do some extra filtering
        # Seen as we already have all the speeds and thy all have ratio's already
        # we don't need to make another database call here, we can just
        # only add the relevant results to our resopnse list
        if ratio != "all":
            # for each cassette in the speeds list
            for item in speeds:
                # check if the ratio is the one we requested
                if item.ratio == ratio:
                    # if it was, add it to the response list
                    response.append(item)
        # otherwise, ratio was all, so we just add everything to the response list.
        else:
            for item in speeds:
                response.append(item)

        # and finally, return the jsonify-ied response
        return jsonify(response)

    # Handle 8 speed queries
    if speed == '8':
        if ratio != "all":
            return jsonify(get_speed_ratio_8spd(ratio))
        else:
            return jsonify(get_speed_8spd_all())

    # Handle 9 speed queries
    if speed == '9':
        if ratio != "all":
            return jsonify(get_speed_ratio_9spd(ratio))
        else:
            return jsonify(get_speed_9spd_all())

    # Handle 10-speed queries
    if speed == '10':
        if ratio != "all":
            return jsonify(get_speed_ratio_10spd(ratio))
        else:
            return jsonify(get_speed_10spd_all())

    # Handle 11 speed queries
    if speed == '11':
        if ratio != "all":
            return jsonify(get_speed_ratio_11spd(ratio))
        else:
            return jsonify(get_speed_11spd_all())

    # Presumably there would also be 12 speed at some point?

    # return a success message with an error message inside
    return jsonify({"error": "query not supported"})


# This function is for when multiple options are selected, needs work, currently show TypeError with missing required argument: 'speed'
# @app.route("/ratio_speed/<ratio>/<speed>")
# def ratio_speed_list(ratio, speed):
#     print(f"Ratio Query: {ratio, speed}")
#     return jsonify(get_ratio_speed_10spd(ratio, speed))

# This is another way to run this function
# @app.route("/speed/<speed>")
# def speed_list(speed):
#     if speed == '8':
#         return jsonify(get_brand_8spd_all("*"))
#     elif speed == '9':
#         return jsonify(get_brand_9spd_all("*"))
#     elif speed == '10':
#         return jsonify(get_brand_10spd_all("*"))
#     elif speed == '11':
#         return jsonify(get_brand_11spd_all("*"))
#     else:
#         return jsonify({"message: no more speeds bro"})


@app.route("/speedratio/8/<ratio>")
def speed_ratio_list_8spd(ratio):
    print(f"Ratio Speed Query: {ratio}")
    return jsonify(get_speed_ratio_8spd(ratio))


@app.route("/speedratio/9/<ratio>")
def speed_ratio_list_9spd(ratio):
    print(f"Ratio Speed Query: {ratio}")
    return jsonify(get_speed_ratio_9spd(ratio))

@app.route("/speedratio/10/<ratio>")
def speed_ratio_list_10spd(ratio):
    print(f"Ratio Speed Query: {ratio}")
    return jsonify(get_speed_ratio_10spd(ratio))

@app.route("/speedratio/11/<ratio>")
def speed_ratio_list_11spd(ratio):
    print(f"Ratio Speed Query: {ratio}")
    return jsonify(get_speed_ratio_11spd(ratio))

if __name__ == "__main__":
    app.run(debug=True)
