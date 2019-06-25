import unittest
import sys
#sys.path.append("..")
from utils import tools as tools


class tools_test(unittest.TestCase):


	def setUp(self):
		self.aliments_existants = ['Pico de Gallo', 'cornmeal', 'filletsole', 'maple extract', 'vinaigrette']
		self.aliments_inexistants = ['queue de rat', 'oeil de triton', 'Bave de crapaud']
		self.aliments_a_testes = ['vinaigrette', 'queue de rat', 'maple extract', 'cornmeal', 'Bave de crapaud',
									 'filletsole', 'Pico de Gallo', 'oeil de triton']

	def test_ingredients_exitants(self):
		res = tools.checkIfIngredientsExist(self.aliments_a_testes)
		for aliment in res[0]:
			self.assertTrue(aliment in self.aliments_existants)


	def test_ingredients_inexitants(self):
		res = tools.checkIfIngredientsExist(self.aliments_a_testes)
		for aliment in res[1]:
			self.assertTrue(aliment in self.aliments_inexistants)

	def test_existance(self):
		res = tools.checkIfIngredientsExist(self.aliments_a_testes)
		self.assertTrue(len(res) == 2)
		self.assertTrue(len(res[0]) == 5)
		self.assertTrue(len(res[1]) == 3) 


if __name__ == '__main__':
    unittest.main()
