import sys

import pandas as pd

sys.path.append("..")
from src import user


def csvToPanda(file, sep=","):
    return pd.read_csv(file, sep=sep)

def idToUser(users_list):
    res = []
    for id in users_list:
        res.append(user.User(id))
    return res


'''
    Cette méthode retourne une liste d'ingrédients pour compléter la recette recommandée
    Paramtères : 
    recipe_ingredients : représente une seule recette, c'est une liste d'ingrédients
    fridge_ingredients : représente le contenu du frigo de l'utilisateur, c'est une liste d'ingrédients
    Return : Liste d'ingrédients pour compléter la recette
'''
def get_ingredients_to_buy(recipe_ingredients, fridge_ingredients) :
    return list(set(recipe_ingredients) - set(fridge_ingredients))




#if __name__ == '__main__' :
#    fridge = ['fromage', 'lait', 'banane']
#    ingredients = ['fromage', 'lait', 'creme fraiche']

#    print(get_ingredients_to_buy(ingredients, fridge))