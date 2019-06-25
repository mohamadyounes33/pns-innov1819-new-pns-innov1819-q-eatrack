import sys
import unittest

sys.path.append("..")
from src.group_recommender import *

import os

package_dir = os.path.dirname(os.path.abspath(__file__))
resource_file_path = os.path.join(package_dir,'../Res/clean_recipes.csv')

recipes = pd.read_csv(resource_file_path, sep=';')


class TestPreferences(unittest.TestCase):
    def setUp(self):
        self.myRecommendations = recipes[recipes["Ingredients"].str.contains("flour")]
        self.mydislikes = ["oil", "butter"]

    def test_remove_allergic_recipes(self):
        """
        This is a test to remove allergic recipes using a list of allergic or disliked ingredients
        :return: success or failure of tests that check if the filtered recipes contain allergic/disliked ingredients
        after filtering
        """
        self.nbrBeforeFiltering = self.myRecommendations.shape[0]
        self.filteredRec = remove_dislikes(self.myRecommendations, self.mydislikes)
        self.nbrAfterFiltering = self.filteredRec.shape[0]
        self.assertNotEqual(self.nbrBeforeFiltering, self.nbrAfterFiltering, msg="The number of recommended recipes "
                                                                                 "should not be the same after filtering by "
                                                                                 "dislikes")
        self.assertTrue(self.filteredRec[self.filteredRec["Ingredients"].str.contains("oil")].empty, msg="The table "
                                                                                                         "should not "
                                                                                                         "contains any "
                                                                                                         "recipe that "
                                                                                                         "contains oil")
        self.assertTrue(self.filteredRec[self.filteredRec["Ingredients"].str.contains("butter")].empty, msg="The table "
                                                                                                            "should not "
                                                                                                            "contains any "
                                                                                                            "recipe that "
                                                                                                            "contains butter")

    def test_dislikes_removed_recommendation(self):
        """
        This test verify if there are no recommendation for users who disliked a certain ingredient
        :return: success of failure of tests
        """
        self.users = [204837, 77852]

        self.dislikes = union_group_undesirable(idToUser(self.users))
        self.recommendations = aggregated_voting(self.users)
        for recipe in self.recommendations:
            for ingredient in self.dislikes:
                self.assertFalse(ingredient in recipe["Ingredients"], msg="Recommended recipes should not have "
                                                                          "any disliked ingredient: ")


if __name__ == '__main__':
    unittest.main()
