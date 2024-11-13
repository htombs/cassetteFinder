from flask import Flask, jsonify
from flask_cors import CORS
from database.cassette_finder_script import get_speed_8spd_all, get_speed_9spd_all, get_speed_10spd_all, get_speed_11spd_all
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
                if item['ratio'] == ratio:
                    # if it was, add it to the response list
                    response.append(item)
        # otherwise, ratio was all, so we just add everything to the response list.
        else:
            for item in speeds:
                response.append(item)
    
        if brand != "all":
            for item in speeds:
                if item[brand] == brand:
                    response.append(item)
        else:
            for item in speeds:
                response.append(item)

        # and finally, return the jsonify-ied response
        return jsonify(response)

    # Handle 8 speed queries
    if speed == '8':
        if ratio != "all":
            return jsonify(get_speed_ratio_brand_8spd(ratio, brand))
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

    print(f"Ratio Speed Query: {ratio}")
    return jsonify(get_speed_ratio_11spd(ratio))

if __name__ == "__main__":
    app.run(debug=True)
