import sys
import unittest

import pandas as pd

sys.path.append("..")

from src import user_profil as user_profil

class user_profil_test(unittest.TestCase) :

    """Test case utilisé pour tester les fonctionnalités du module user_profil"""

    def setUp(self):
        self.user_profil_under_test = user_profil.User_Profil(675719)
        self.user_profil_under_test.set_db_test()  # set test database for this test case
        self.preferences_to_add = ['coconut', 'artichoke']
        self.allergies_to_add = ['lemon', 'macaroni']
        self.allergies_to_remove_not_found = ['spice', 'tart', 'sugar']
        self.preferences_to_remove_not_found = ['wasabi', 'wheat', 'gluten']
        self.user_fridge_depart = ['milk','apple']
        self.ingredients_to_add_fridge = ['coconut', 'onion']
        self.existant_ingredients_to_remove_fridge = self.ingredients_to_add_fridge
        self.remaining_ingredients_fridge = ['onion']
        self.inexistant_ingredients_to_remove_fridge = ['parmesan', 'coconut']
        self.not_found_ingredients = [['coconut'],['parmesan'],[]]


    # story 30
    def test_user_profil_add_remove_preferences(self):

        initial_preferences_count = len(self.user_profil_under_test.get_preferences())
        print(self.user_profil_under_test.get_preferences())
        print(self.preferences_to_add)
        ''' adding preferences '''
        self.user_profil_under_test.add_preference(self.preferences_to_add)
        new_preferences_count = len(self.user_profil_under_test.get_preferences())
        self.assertEqual(new_preferences_count, initial_preferences_count + len(self.preferences_to_add))


        ''' removing preferences '''
        self.user_profil_under_test.remove_preferences(self.preferences_to_add)
        new_preferences_count = len(self.user_profil_under_test.get_preferences())
        self.assertEqual(new_preferences_count, initial_preferences_count)



    def test_user_profil_add_allergies(self):
        initial_allergies_count = len(self.user_profil_under_test.get_allergies())

        ''' adding allergies '''
        self.user_profil_under_test.add_allergies(self.allergies_to_add)
        new_allergies_count = len(self.user_profil_under_test.get_allergies())
        self.assertEqual(new_allergies_count, initial_allergies_count + len(self.allergies_to_add))

        ''' removing allergies '''
        self.user_profil_under_test.remove_allergies(self.allergies_to_add)
        new_allergies_count = len(self.user_profil_under_test.get_allergies())
        self.assertEqual(new_allergies_count, initial_allergies_count)


    def test_user_profil_remove_allergies_not_found(self):
        ''' removing not found allergies '''
        not_found = []
        not_found = self.user_profil_under_test.remove_allergies(self.allergies_to_remove_not_found)

        self.assertEqual(len(not_found), len(self.allergies_to_remove_not_found))

    def test_user_profil_remove_preferences_not_found(self):
        ''' removing not found preferences '''
        not_found = []
        not_found = self.user_profil_under_test.remove_preferences(self.preferences_to_remove_not_found)

        self.assertEqual(len(not_found), len(self.preferences_to_remove_not_found))


    def test_user_profil_add_remove_ingredients_fridge(self):
        ''' checking initial content '''
        #self.assertEqual(self.user_profil_under_test.get_fridge(), self.user_fridge_depart)

        ''' adding ingredients '''
        self.user_profil_under_test.add_ingredients_fridge(self.ingredients_to_add_fridge)

        ''' removing ingredients '''
        not_found = self.user_profil_under_test.remove_ingredients_fridge(self.existant_ingredients_to_remove_fridge)
        #self.assertEqual(not_found, [])



    def test_user_profil_remove_inexistant_ingredients_fridge(self):
        ''' adding ingredients '''
        self.user_profil_under_test.add_ingredients_fridge(self.ingredients_to_add_fridge)

        ''' removing inexistant ingredients '''
        not_found = self.user_profil_under_test.remove_ingredients_fridge(self.inexistant_ingredients_to_remove_fridge)

        self.assertEqual(not_found, self.not_found_ingredients)

    def test_user_profil_clear_fridge(self):
        ''' adding ingredients '''
        self.user_profil_under_test.add_ingredients_fridge(self.ingredients_to_add_fridge)

        ''' cleaning ingredients '''
        self.assertNotEqual(self.user_profil_under_test.get_fridge(), [])
        self.user_profil_under_test.clear_fridge()
        self.assertEqual(self.user_profil_under_test.get_fridge(), [])

    def test_user_delete_history(self):
        # the user's history is initially not empty
        self.assertNotEqual(self.user_profil_under_test.get_history(), [],
                            "The history list of the actual user should not be empty")
        # deleting user's history
        backup = self.user_profil_under_test.delete_history()
        # the user's history is now empty
        self.assertEqual(self.user_profil_under_test.get_history(), [],
                         "The history list of the actual user should be empty")
        # after testing, revert to the old csv file
        pd.DataFrame(backup).to_csv(self.user_profil_under_test.resource_file_history_path, sep=",", index=False)


if __name__ == '__main__':
    unittest.main()