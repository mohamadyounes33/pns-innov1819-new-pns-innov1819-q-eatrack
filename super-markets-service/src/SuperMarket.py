
class SuperMarket:
    """
    a class to mock supermarkets, defined by an id, a name, gps coordination and a dictionary of items
    """
    # Attributes

    def __init__(self, id):
        """
        the constructor of the supermarket class
        :param id: the id number of the supermarket
        """
        self.__id = id
        self.__gps_coordinates = [-1, -1]
        self.__items = {}
        self.__name = ""



    def set_name(self, name):
        """
        set the name of the supermarket, carrefour for example
        :param name: a string containing the name of the shop to be set
        """
        self.__name = name



    def set_gps_coordinates(self, latitude, longitude):
        """
        set the coordinates of the supermarket
        :param latitude: latitude coordinate of the supermarket
        :param longitude: longitude coordinate of the supermarket
        """
        self.__gps_coordinates = [latitude, longitude]


    def set_items(self, items):
        """
        set the items products of a supermarket
        :param items: a dictionary that contains products as key and a pair of {price, discount}
        """
        self.__items = items

    def add_item(self, item):
        """
        add an item / product to the list of items
        :param item: a triplet of item, price, discount
        :return:
        """
        self.__items[item[0]] = [item[1], item[2]]

    def add_items(self, items):
        for i in items:
            self.__items[i[0]] = [i[1], i[2]]

    # ---------- Getters -----------
    def get_items(self):
        return self.__items

    def get_location(self):
        return self.__gps_coordinates

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_discounts(self):
        """
        this method returns the list of products of a shop that have discount
        """
        return [i for i in self.__items.items() if i[1][1] > 0]

    def __str__(self):
        return str(self.__id)+ ": " + self.__name


if __name__=="__main__":
    carrefour = SuperMarket(1)
    carrefour.set_gps_coordinates(2, 5)
    carrefour.set_name("Carrefour Market")
    carrefour.add_item(["oil", 5, 0.5])
    carrefour.add_items([["eggs", 2, 0.3], ["flour", 3, 0.4], ["chicken",6, 0.8]])
    print(carrefour.get_items())
    print(carrefour.get_discounts())
