import requests
from flask import Flask, jsonify, Response, request

from src.SM_rec import get_ingredients_to_buy, mock_markets, recommend_shops, get_supermarket_details

app = Flask(__name__)


# root to get user's localization from localization service
@app.route("/getLocalization", methods=['GET'])
def send_my_localization():
    r = requests.get("http://localhost:8181/getLocalization")

    return Response(
        r.text,
    status = r.status_code,
             content_type = r.headers['content-type'],)


# root to get user's fridge in order to calculate missing ingredients
@app.route("/getFridge/<id>")
def get_fridge(id):
    print("id === "+str(id))
    r = requests.get("http://localhost:8080/getUserFridge/"+id)
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content-type'], )


# root to get missing ingredients from Client (CLI or IHM)
'''@app.route("/missingIngredients", methods=['POST'])
def missing_ingredients():
    input = request.args
    missing_ingredients= input['missing_ingredients']
    missing_ingredients = ast.literal_eval(missing_ingredients)

    print("################")
    print("In SuperMarkets, Missing ingredients received :")
    for ingredient in missing_ingredients :
        print(ingredient)
    print("################")

    result = None  # replace result by calling method to deal with supermarkets list

    #return str(result)
    return str(0)'''

"""
This route is used to get the list of partner shops sorted by discounts
"""
@app.route("/getShops", methods=['POST'])
def get_shops():

    input = request.json
    ingredients = input['ingredients']
    ingredients = ingredients.split(",")
    user_id = input['id']
    # Get the user's location
    userPosition = send_my_localization().json
    userPosition = [float(userPosition['latitude']), float(userPosition['longitude'])]
    print("################")
    print("In SuperMarkets, Missing ingredients received : ", ingredients)
    print("################")
    # calculate missing ingredients
    fridge = get_fridge(user_id).json["fridge"]
    print("################")
    print("User's fridge: ", fridge)
    missing_ingredients = get_ingredients_to_buy(ingredients, fridge)
    print("################")
    print("Ingredients to buy: ", missing_ingredients)
    # TODO delete this list of mocked shops
    shops = mock_markets()
    recommended_shops = recommend_shops(shops, userPosition, missing_ingredients)
    # print(recommended_shops)
    res = {'shops': []}
    for m in recommended_shops:
        market = {}
        market['name'] = m[0]
        market['distance'] = m[1]
        market['total price'] = m[2]
        res['shops'].append(market)

    tmp = jsonify(res)
    print(str(tmp.json))
    return str(tmp.json)


"""
This route is used to get the detail of discount ingredients in the given supermarket
"""
@app.route("/getSuperMarketDetails", methods=['POST'])
def get_sm_details():

    input = request.json
    ingredients = input['ingredients']
    id = input['id']

    details = get_supermarket_details(id, ingredients)
    print("################")
    print("details = "+str(details))
    print("################")
    
    res = {}
    res['details'] = details
    tmp = jsonify(res)

    print(str(tmp.json))
    return str(tmp.json)



if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8585, debug=True)
