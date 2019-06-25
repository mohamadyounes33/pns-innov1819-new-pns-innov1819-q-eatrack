'''
    This program manage preferences and dislikes of group of users
'''

import os

import numpy as np
import pandas as pd

from src.user import User

path = os.path.dirname(os.path.realpath(__file__))

recipes = pd.read_csv(path + "/../Res/clean_recipes.csv", sep=";")


package_dir = os.path.dirname(os.path.abspath(__file__))
resource_file_path = os.path.join(package_dir,'../Res/clean_recipes.csv')

all_recipes = pd.read_csv(resource_file_path, sep=';')



# function to get a group of preferences (ingedients) set
# parameters : group_df : group of users
# return : dictionnary giving to every ingredient the number of occurences in the group of users
def union_group_preferences(user_list):
    preferences = []
    for i in user_list:
        preferences += personal_preference(i)
    preferences = np.array(preferences)
    unique, counts = np.unique(preferences, return_counts=True)

    return dict(zip(unique, counts))


def personal_preference(user):
    """
    This function return the preferences of a certain user based on the csv file of profiles
    :param userId: the id of the user
    :return: a list of preferences of that user
    """
    return user.get_preferences()


def remove_dislikes(recipes, dislikes):
    dislikes_str = "|".join(dislikes)
    allergic_recipes = recipes[recipes["Ingredients"].str.contains(dislikes_str)]
    return recipes[~recipes["RecipeID"].isin(allergic_recipes["RecipeID"])]


def contains_ingredient_nbr(recipe, ingredients):
    score = 0
    for ing in ingredients:
        if recipes[recipes["RecipeID"] == int(recipe)]["Ingredients"].str.contains(ing).values[0]:
            score += 1
    return score


# function to get a group of dislikes (ingredients) set
# parameters : group_df : group of users
# return : dictionary giving to every ingredient the number of occurrences in the group of recipes
def union_group_undesirable(user_list):
    undesirable = []
    for i in user_list:
        if (i.get_allergies() != ['']):
            undesirable += i.get_allergies()
    return list(set().union(undesirable))


if __name__ == "__main__":
    # test
    user1 = User(2942936)
    user2 = User(4520736)
    group = [user1, user2]
    print(union_group_preferences(group))
    # print(union_group_undesirable(group))
    #print(personal_preference(user1))
