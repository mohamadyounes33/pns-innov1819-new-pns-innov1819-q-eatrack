from flask import Flask, request, jsonify
import src.User_localization as ul

app = Flask(__name__)


# root to get user's localization, executing chromedriver
@app.route("/getLocalization", methods=['GET'])
def send_my_localization():
    my_localization = ul.getLocation()

    res = {}
    res['latitude'] = my_localization[0]
    res['longitude'] = my_localization[1]
    res['statut'] = 0

    json_res = jsonify(res)

    return json_res



if __name__ == '__main__':
    app.run(host='localhost', port=8181, debug=True)
