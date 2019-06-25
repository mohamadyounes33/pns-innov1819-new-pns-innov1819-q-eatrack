import unittest
import sys
#sys.path.append("..")
from src import frigo as fridge_module


class frigo_test(unittest.TestCase):

	"""Test case utilisé pour tester les fonctionnalités du module frigo"""

	def setUp(self):
		self.frigo_content_depart = ['fraise', 'lait', 'banane']
		self.ingredient_to_add = 'chocolat'
		self.ingredients_list_to_add = ['cornichon, concombre']
		self.frigo_under_test = fridge_module.Frigo(self.frigo_content_depart)
		self.ingredient_to_remove = 'lait'
		self.ingredients_list_to_remove = ['fraise', 'banane']
		self.inexistant_ingredient = 'citron'
		self.inexistant_list_ingredients = ['pomme', 'fromage']

	def test_add_ingredient(self) :
		"""Test fonction add_frigo."""
		self.assertEqual(self.frigo_under_test.get_fridge(), self.frigo_content_depart)

		self.assertFalse(self.ingredient_to_add in self.frigo_under_test.get_fridge())
		self.frigo_under_test.add_in_fridge(self.ingredient_to_add)
		self.assertTrue(self.ingredient_to_add in self.frigo_under_test.get_fridge())

	def test_add_list_ingredients(self) :
		"""Test fonction add_frigo with list in arguments."""
		self.frigo_under_test.add_in_fridge(self.ingredients_list_to_add)
		self.assertTrue(self.ingredients_list_to_add in self.frigo_under_test.get_fridge())


	def test_remove_ingredient(self) :
		"""Test fonction remove ingredient."""
		self.assertTrue(self.ingredient_to_remove in self.frigo_under_test.get_fridge())
		self.frigo_under_test.remove_ingredient(self.ingredient_to_remove)
		self.assertTrue(self.ingredient_to_remove not in self.frigo_under_test.get_fridge())

	def test_remove_list_ingredients(self) :
		"""Test fonction remove with list in arguments."""
		for ingredient in self.ingredients_list_to_remove :
			self.assertTrue(ingredient in self.frigo_under_test.get_fridge())

		self.frigo_under_test.remove_list_ingredients(self.ingredients_list_to_remove)
		self.assertTrue(self.ingredients_list_to_remove not in self.frigo_under_test.get_fridge())

	def test_remove_ngredients_with_inexistant_ingredient(self) :
		"""Test fonction remove with inexistant arguments."""
		self.assertTrue(self.inexistant_ingredient not in self.frigo_under_test.get_fridge())
		self.frigo_under_test.remove_ingredient(self.inexistant_ingredient)
		self.assertTrue(self.inexistant_ingredient not in self.frigo_under_test.get_fridge())

	def test_remove_list_ingredients_with_inexistant_ingredient(self) :
		"""Test fonction remove with inexistant list in arguments."""
		for ingredient in self.inexistant_list_ingredients :
			self.assertTrue(ingredient not in self.frigo_under_test.get_fridge())

		self.frigo_under_test.remove_list_ingredients(self.inexistant_list_ingredients)
		self.assertTrue(self.inexistant_list_ingredients not in self.frigo_under_test.get_fridge())





if __name__ == '__main__':
    unittest.main()
