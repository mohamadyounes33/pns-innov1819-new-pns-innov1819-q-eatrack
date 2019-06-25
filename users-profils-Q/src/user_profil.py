'''
	This program is a handler to retrieve user's profile from data base.
	It stores user_id, preferences, allergies and history.
'''
import csv
import os

import pandas as pd

from src import frigo as fridge
from utils import tools as tools

package_dir = os.path.dirname(os.path.abspath(__file__))



class User_Profil:
    # attributs
    user_id = None
    preferences = []
    allergies = []
    frigo = None
    history = []
    resource_file_path = os.path.join(package_dir, '../Res/generated_profiles.csv')
    resource_file_fridge_path = os.path.join(package_dir, '../Res/fridge_content.csv')
    resource_file_history_path = os.path.join(package_dir, '../Res/clean_reviews.csv')

    # constructor
    # parameters : user_id : the user_id to retrieve from the data base
    def __init__(self, user_id):
        # with open('Res/generated_profiles.csv', 'r') as profiles :
        with open(User_Profil.resource_file_path, 'r') as profiles:
            reader = csv.reader(profiles, delimiter=';')
            for row in reader:
                if str(row[0]) == str(user_id):
                    self.set_user_id(row)
                    self.set_preferences(row)
                    self.set_allergies(row)
                    self.set_history()
                    # self.frigo = fridge.Frigo([])
                    self.frigo = fridge.Frigo(tools.get_fridge_content(user_id))
            if self.user_id == None:
                raise ValueError("User not found !")
        # raise UnknowknIdException('user with id = {} is not found.\n',format(user_id))
        # raise Exception('user with id = {} is not found.\n',format(user_id))

    # function to set the user_id
    # parameters :  row : readed row from database
    def set_user_id(self, row):
        self.user_id = row[0]

    # function to set allergies list
    # parameters : row : readed row from database
    def set_allergies(self, row):
        self.allergies = row[2].split(',')

    # function to set preferences list
    # parameters : row : readed row from database
    def set_preferences(self, row):
        self.preferences = row[1].split(',')

    # function to add a preference to a list
    # it adds row in csv file data base
    # parameters : preference to add
    def add_preference(self, preferencesToAdd):


        ingredientsExistence = tools.checkIfIngredientsExist(preferencesToAdd)
        res = [[],[],[]]
        res[2] = ingredientsExistence[1]

        for preference in ingredientsExistence[0]:
            if not (preference in self.preferences):
                self.preferences.append(preference)
                res[0].append(preference)
            else :
                res[1].append(preference)

        # add row in csv file data base
        tools.addInFile(self, User_Profil.resource_file_path, 'preferences', ingredientsExistence[0])
        return res

    # function to set history (tried recipes)
    # parameters : row : readed row from database
    def set_history(self):
        self.history = []
        with open(User_Profil.resource_file_history_path, 'r') as reviews:
            reader = csv.reader(reviews, delimiter=',')
            for row in reader:
                if str(row[1]) == str(self.user_id):
                    self.history.append(int(row[0]))


    # function to remove a preference from the list
    # it removes row from csv file data base
    # parameters : preference to remove
    # returns list of not found preferences asked to be deleted
    def remove_preferences(self, preferencesToRemove):


        ingredientsExistence = tools.checkIfIngredientsExist(preferencesToRemove)
        res = [[],[],[]]
        res[2] = ingredientsExistence[1]
        # list of not found preferences to delete
        #not_found = []

        for preference in ingredientsExistence[0]:
            if preference in self.preferences:
                self.preferences.remove(preference)
                res[0].append(preference)
            else:
                #not_found.append(preference)
                res[1].append(preference)

                # add row in csv file data base
        tools.removeInFile(self, User_Profil.resource_file_path, 'preferences', ingredientsExistence[0])

        return res

    # function to add a allergie to a list
    # it adds add row in csv file data base
    # parameters : allergies to add
    # returns list of not found allergies asked to be deleted
    def add_allergies(self, allergiesToAdd):


        ingredientsExistence = tools.checkIfIngredientsExist(allergiesToAdd)
        res = [[],[],[]]
        res[2] = ingredientsExistence[1]

        for allergie in ingredientsExistence[0]:
            if not (allergie in self.allergies):
                self.allergies.append(allergie)
                res[0].append(allergie)
            else:
                res[1].append(allergie)

                # add row in csv file data base
        tools.addInFile(self, User_Profil.resource_file_path, 'undesirable', ingredientsExistence[0])
        return res

    # function to remove a preference from the list
    # it removes row from csv file data base
    # parameters : preference to remove
    def remove_allergies(self, allergiesToRemove):


        ingredientsExistence = tools.checkIfIngredientsExist(allergiesToRemove)
        res = [[],[],[]]
        res[2] = ingredientsExistence[1]
        # list of not found allergies to delete
        #not_found = []

        for allergie in ingredientsExistence[0]:
            if allergie in self.allergies:
                self.allergies.remove(allergie)
                res[0].append(allergie)
            else:
                #not_found.append(allergie)
                res[1].append(allergie)

                # add row in csv file data base
        tools.removeInFile(self, User_Profil.resource_file_path, 'undesirable', ingredientsExistence[0])

        return res

    def delete_history(self):
        """
        This method is used to remove all history records of this user, which means deletions of all
        his entries is the clean_reviews.csv file
        :return:
        """
        # read the clean_reviews csv file
        reviews = pd.read_csv(User_Profil.resource_file_history_path, sep=",")
        # select columns that are not of this current user
        new_reviews = reviews[reviews["profileID"] != int(self.user_id)]
        # overwrite the reviews with new ones that doesnt contains entries of current user
        pd.DataFrame(new_reviews).to_csv(User_Profil.resource_file_history_path, sep=",", index=False)
        self.history = []
        return reviews


    def add_ingredients_fridge(self, ingredients_to_add):


        ingredientsExistence = tools.checkIfIngredientsExist(ingredients_to_add)
        res = [[],[],[]]
        res[2] = ingredientsExistence[1]
        for ingredient in ingredientsExistence[0]:
            if not (ingredient in self.frigo.get_content()):
                self.frigo.add_in_fridge(ingredient)
                res[0].append(ingredient)
            else:
                res[1].append(ingredient)

        # add row in csv file data base
        tools.addInFile(self, User_Profil.resource_file_fridge_path, 'content', ingredientsExistence[0])
        return res

    def remove_ingredients_fridge(self, ingredients_to_remove):


        ingredientsExistence = tools.checkIfIngredientsExist(ingredients_to_remove)
        res = [[],[],[]]
        res[2] = ingredientsExistence[1]

        for ingredient in ingredientsExistence[0]:
            if ingredient in self.frigo.get_content():
                self.frigo.remove_ingredient(ingredient)
                res[0].append(ingredient)
            else:
                res[1].append(ingredient)

        tools.removeInFile(self, User_Profil.resource_file_fridge_path, 'content', ingredientsExistence[0])
        return res

    def clear_fridge(self):
        ingredients_to_remove = []
        for ingredient in self.get_fridge():
            ingredients_to_remove.append(ingredient)

        tools.removeInFile(self, User_Profil.resource_file_fridge_path, 'content', ingredients_to_remove)

        self.frigo.clear_fridges()

        return self.get_fridge()

    """			getters 			"""

    def get_preferences(self):
        return self.preferences

    def get_allergies(self):
        return self.allergies

    def get_user_id(self):
        return self.user_id

    def get_fridge(self):
        return self.frigo.get_fridge()

    def get_history(self):
        return self.history

    """
        Fonction to modify data base path with the set one
        It is only used in test cases, in setup method
    """
    def set_db_test(self):
        User_Profil.resource_file_fridge_path = os.path.join(package_dir, '../Res/test_db_fridge_content.csv')
        User_Profil.resource_file_path = os.path.join(package_dir, '../Res/test_db_generated_profiles.csv')
        User_Profil.resource_file_history_path = os.path.join(package_dir, '../Res/test_db_history.csv')

if __name__ == "__main__" :
    #u = User_Profil(413121)

    u = User_Profil(2785736)
    # u.remove_ingredients_fridge(['test'])
    print(u.get_history())
    #u.delete_history()
    #u.add_preference(['zbi_2', 'xxxxxx', 'yyyy'])
    #addInFile(1099951, resource_file_path, "content", ['haha', 'xx', 'bbb', 'cc'])
#    user = User_Profil(675719)
#    liste = ["egg"]
#    user.remove_preferences(liste)
#    print(user.get_preferences())
