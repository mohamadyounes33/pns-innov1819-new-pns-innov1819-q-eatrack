import sys
import unittest
from collections import OrderedDict

#sys.path.append("..")

from src.client_side import profiles_service_requester as rq
import pandas as pd
import os


package_dir = os.path.dirname(os.path.abspath(__file__))

class profiles_service_requester_test(unittest.TestCase):

    """Test case utilisé pour tester les fonctionnalités du module profile_service_requester"""

    def setUp(self):
        self.frigo_content_depart = ['fraise', 'lait', 'banane']
        self.existant_ids_group = [675719, 539102, 2810501]
        self.existant_id = 675719
        self.existant_id_empty_fridge = 1896099             # pas utilisé pour l'instant !
        self.incorrect_ids_group = [33, 25495, 675719]
        self.inexistant_id = 000

        self.resource_profiles_file = os.path.join(package_dir, '../Res/generated_profiles.csv')
        self.resource_fridge_file = os.path.join(package_dir, '../Res/fridge_content.csv')
        self.resource_history_file = os.path.join(package_dir, '../Res/clean_reviews.csv')

        profiles_file = pd.read_csv(self.resource_profiles_file, sep=";")
        fridge_file = pd.read_csv(self.resource_fridge_file, sep=";")
        history_file = pd.read_csv(self.resource_history_file, sep=",")
        #print("\n")
        #print(profiles_file[profiles_file['user_id'] == int(self.existant_id)])

        df_profiles = profiles_file[profiles_file['user_id'] == int(self.existant_id)]
        df_fridge = fridge_file[(fridge_file['user_id'] == int(self.existant_id))]
        df_history = history_file[(history_file['profileID'] == int(self.existant_id))]

        self.actual_preferences_existant_user = df_profiles['preferences'].values.tolist()[0].split(',')
        self.actual_allergies_existant_user = df_profiles['undesirable'].values.tolist()[0].split(',')
        self.actual_fridge_existant_user = df_fridge['content'].values.tolist()[0].split(',')
        self.actual_history_existant_user = df_history['RecipeID'].values.tolist()

        self.actual_preferences_existant_group_user = []
        self.actual_allergies_existant_group_user = []
        self.actual_fridge_existant_group_user = []
        self.actual_history_existant_group_user = []

        for id in self.existant_ids_group:
            df_profiles = profiles_file[(profiles_file['user_id'] == int(id))]
            df_fridge = fridge_file[(fridge_file['user_id'] == int(id))]
            df_history = history_file[(history_file['profileID'] == int(id))]

            self.actual_preferences_existant_group_user += df_profiles['preferences'].values.tolist()[0].split(',')
            self.actual_allergies_existant_group_user += df_profiles['undesirable'].values.tolist()[0].split(',')
            self.actual_history_existant_group_user += df_history['RecipeID'].values.tolist()
            self.actual_history_existant_group_user = list(OrderedDict.fromkeys(self.actual_history_existant_group_user))

            if str(id) == str(self.existant_ids_group[0]) :
                self.actual_fridge_existant_group_user += df_fridge['content'].values.tolist()[0].split(',')

    def test_get_user_profil_existant(self):
        """Test case utilisé pour tester récupération du profil d'un utilisateur existant"""
        profil = rq.get_user_profil(self.existant_id)
        self.assertEqual(profil[0], self.actual_preferences_existant_user)
        self.assertEqual(profil[1], self.actual_allergies_existant_user)
        self.assertEqual(profil[2], self.actual_fridge_existant_user)
        self.assertEqual(profil[3], self.actual_history_existant_user)
        self.assertEqual(profil[4], 0)

    def test_get_user_profil_inexistant(self):
        """Test case utilisé pour tester récupération du profil d'un utilisateur inexistant"""
        profil = rq.get_user_profil(self.inexistant_id)
        self.assertEqual(profil[4], -1)

    def test_get_group_users_profil_existant(self):
        """Test case utilisé pour tester récupération du profil d'un utilisateur inexistant"""
        profils = rq.get_group_profils(self.existant_ids_group)

        self.assertEqual(profils[0], self.actual_preferences_existant_group_user)
        self.assertEqual(profils[1], self.actual_allergies_existant_group_user)
        self.assertEqual(profils[2], self.actual_fridge_existant_group_user)
        self.assertEqual(profils[3], self.actual_history_existant_group_user)

    def test_get_group_users_profil_not_existant(self):
        """Test case utilisé pour tester récupération du profil d'un groupe d'utilisateurs inexistants"""
        profils = rq.get_group_profils(self.incorrect_ids_group)
        self.assertEqual(profils[4], -1)
if __name__ == '__main__':
    unittest.main()
