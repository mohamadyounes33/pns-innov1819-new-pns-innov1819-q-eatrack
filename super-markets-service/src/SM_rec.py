import operator

from math import sin, cos, sqrt, atan2, radians

from src.SuperMarket import SuperMarket


def getUserLocation(user):
    """
    This function is used to call the user's method getlocation that returns his gps coordinates
    :param user: a user
    :return: the user's location
    """
    return user.getLocation()


def distanceFromUser(shopCoord, userCoord):
    """
    This function calculate the distance between the user and a supermarket using their gps coordinates
    :param shopCoord: a pair of latitude/longitude coordinates of the market
    :param userCoord: a pair of latitude/longitude coordinates of the user
    :return: the distance in km between the user and the market
    """
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(shopCoord[0])
    lon1 = radians(shopCoord[1])
    lat2 = radians(userCoord[0])
    lon2 = radians(userCoord[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


def get_near_markets(marketlist, userPosition, range=float("infinity")):
    """
    This function return a list of markets sorted by distance from the user and can be in a range defined by the user
    :param marketlist: a list of markets
    :param range: a range / radius of the location of markets in the nearby of the user
    :return: a list of markets sorted by distance and could be filtered if out of radius
    """
    l = {}
    for m in marketlist:
        distance = distanceFromUser(m.get_location(), userPosition)
        if distance < range:
            l[m] = distance
    sorted_x = sorted(l.items(), key=operator.itemgetter(1))
    return sorted_x


def recommend_shops(markets, userPosition, ingredients):
    """
    function to filter markets that exist nearby the user, then sort them by discounts
    :param markets: a list of all partners
    :param userPosition: the user's position
    :param ingredients: a list of ingredients to buy
    :return: a list of sorted shops
    """
    marketlist = [i[0] for i in get_near_markets(markets, userPosition)]
    score_list = {m: 0 for m in marketlist}
    for m in score_list:
        for ing in ingredients:
            if ing in m.get_items().keys():
                price = (1 - m.get_items()[ing][1]) * m.get_items()[ing][0]
                score_list[m] += price
    sorted_x = sorted(score_list.items(), key=operator.itemgetter(1))
    sorted_shops = [(i[0].get_name(), round(distanceFromUser(i[0].get_location(), userPosition), 2), i[1]) for i in
                    sorted_x if i[1] != 0]
    return sorted_shops

def get_supermarket_details(market_id, ingredients) :
    details = {}
    marketlist = mock_markets()
    for market in marketlist :
        if str(market.get_id()) == str(market_id) :
            for ingredient in ingredients :
                if ingredient in market.get_items().keys() :
                    details[ingredient] = market.get_items()[ingredient][0] * (1 - market.get_items()[ingredient][1])
    return details




def get_ingredients_to_buy(recipe_ingredients, fridge_ingredients):
    """
    Cette méthode retourne une liste d'ingrédients pour compléter la recette recommandée
    :param recipe_ingredients: représente une seule recette, c'est une liste d'ingrédients
    :param fridge_ingredients: représente le contenu du frigo de l'utilisateur, c'est une liste d'ingrédients
    :return: Liste d'ingrédients pour compléter la recette
    """
    return list(set(recipe_ingredients) - set(fridge_ingredients))


def mock_markets():
    """
    this function is used to create 3 static markets that we will use to simulate how we get informations from real ones
    :return: a list of markets
    """
    # first market
    market1 = SuperMarket(1)
    market1.set_name("Carrefour eat")
    market1.set_gps_coordinates(43.710175, 7.261953)
    market1.add_items([["blueberry", 2, 1], ["chicken", 2, 0.5], ["salt", 1, 0.5], ["basil", 3, 0.5], ["black pepper", 2, 0.3], ["salt", 2, 0.5], ["black pepper", 3, 0.15]])
    # second market
    market2 = SuperMarket(2)
    market2.set_name("Casino Cash")
    market2.set_gps_coordinates(43.180145, 7.261153)
    market2.add_items([["basil", 2, 0.5], ["salt", 2, 1], ["salt", 2, 0.2], ["black pepper", 2, 0.1], ["chicken", 6, 0.8],["blueberry", 2, 0.5], ["ketchup", 2, 1], ["black pepper", 2, 0.2], ["eggs", 2, 0.1], ["chicken", 6, 0.8],["blueberry", 2, 0.5], ["ketchup", 2, 1], ["pineapple", 2, 0.2], ["eggs", 2, 0.1], ["chicken", 6, 0.8],["blueberry", 2, 0.5], ["ketchup", 2, 1], ["pineapple", 2, 0.2], ["eggs", 2, 0.1], ["chicken", 6, 0.8]])
    # third market
    market3 = SuperMarket(3)
    market3.set_name("Lidl street")
    market3.set_gps_coordinates(43.790175, 7.228953)
    market3.add_items([["black pepper", 3, 0.4], ["ketchup", 2, 1], ["paprika", 1, 0.5], ["black pepper", 2, 1], ["basil", 2, 0.4], ["flour", 3, 0.3], ["chicken", 6, 0.1]])
    # fourth market
    market4 = SuperMarket(4)
    market4.set_name("Monoprix")
    market4.set_gps_coordinates(43.720175, 7.268903)
    market4.add_items([["mustard", 2, 0.4], ["ketchup", 2, 1], ["black pepper", 1, 0.5]])
    markets = [market1, market2, market3, market4]
    return markets


if __name__ == '__main__':
    userPosition = [43.708425, 7.291667]
    markets = mock_markets()

    print(get_supermarket_details(1, ["blueberry", "cinnamon", "pineapple"]))

    #print(recommend_shops(markets, userPosition, ["oil", "eggs", "chicken"]))
