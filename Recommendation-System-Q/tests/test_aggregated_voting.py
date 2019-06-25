import sys
sys.path.append("..")
from src.group_recommender import aggregated_voting
from flask import Flask

import unittest

class TestAPI(unittest.TestCase):

	def test_open_csv(self):
		app = Flask(__name__)

		with app.app_context():
			response = []
			response = aggregated_voting([618623, 621557])
			self.assertNotEqual(response, [])


if __name__ == '__main__':
    unittest.main()
