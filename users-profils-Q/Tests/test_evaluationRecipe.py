import unittest
import sys
from src import evaluationRecipe as evaluationRecipe
import pandas as pd


class evaluationRecipe_test(unittest.TestCase):

	def setUp(self):
		self.recipeID = 7000
		self.userID = 675719
		self.value = evaluationRecipe.getRate(self.userID, self.recipeID)
		if(self.value == 5.0):
			self.tmp = 2.0
		else:
			self.tmp = 5.0

	def test_evaluationRecipe(self):
		val = evaluationRecipe.getRate(self.userID, self.recipeID)
		self.assertFalse(val == self.tmp)
		self.assertTrue(val == self.value)
		evaluationRecipe.rateRecipe(self.userID, self.recipeID, self.tmp)
		newVal = evaluationRecipe.getRate(self.userID, self.recipeID)
		self.assertTrue(newVal == self.tmp)
		self.assertFalse(newVal == self.value)
		evaluationRecipe.rateRecipe(self.userID, self.recipeID, self.value)


if __name__ == '__main__':
    unittest.main()
