import sys
import unittest

sys.path.append("..")
from src import user as db_reader


class db_reader_test(unittest.TestCase):

	"""Test case utilisé pour tester les fonctionnalités du module db_reader"""

	def setUp(self):
		self.inexistant_id = -1
		self.existant_id = 675719
		self.user = None

	def test_read_profil_inexistant(self) :
		self.assertRaises(Exception, db_reader.User, self.inexistant_id)


	def test_read_profil_existant(self) :
		"""Test récupération d'un profil existant."""
		self.user = db_reader.User(self.existant_id)
		preferences = ['egg', 'rosemary', 'baking powder', 'salsa']
		allergies = ['chocolate', 'brown rice']
		history = ['7000', '8201', '8619', '8749', '8839', '8849', '8945', '10856', '11058', '11587',
			'11771', '11937', '12698', '13981', '14041', '14208', '14497', '14670', '16458', '16458', '16505', '16568', '16664', '17481',
			'17848', '18253', '18352', '18379', '20605', '20849', '22510', '23294', '24421', '25364', '25490', '25676', '25691', '26589']

		self.assertEqual(preferences, self.user.get_preferences())
		self.assertEqual(allergies, self.user.get_allergies())

		#print(history)
		#print("----")
		#print(self.user.get_history())
		#print("-----")
		for recipe in history :
			self.assertTrue(recipe in self.user.get_history())




if __name__ == '__main__':
    unittest.main()
