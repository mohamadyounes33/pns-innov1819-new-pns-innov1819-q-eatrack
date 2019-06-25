'''
	This program is a handler to retrieve user's profile from data base.
	It stores user_id, preferences, allergies and history.
'''
import ast

from src import frigo as fridge
from src.client_side.profiles_service_requester import get_profil


class User :
	
	# attributs
	user_id = None
	preferences = []
	allergies = []
	history = []
	frigo = None


	# constructor
	# parameters : user_id : the user_id to retrieve from the server
	def __init__(self, user_id) :
		request = ast.literal_eval(get_profil(user_id))
		print(request)
		if request != []:
			self.set_user_id(user_id)
			self.set_preferences(request['preferences'])
			self.set_allergies(request['allergies'])
			self.set_history(request['history'])
			self.frigo = fridge.Frigo(request['fridge'])
		else:
			raise Exception('user with id = {} is not found.\n', format(user_id))

					

 	# function to set the user_id
 	# parameters :  row : readed row from database
	def set_user_id(self, id):
		self.user_id = id


	# function to set allergies list
	# parameters : row : readed row from database
	def set_allergies(self, request):
		self.allergies = request


	# function to set preferences list
	# parameters : row : readed row from database
	def set_preferences(self, request):
		self.preferences = request


	# function to set history (tried recipes)
	# parameters : row : readed row from database
	def set_history(self, request):
		self.history = request


	def set_frigo(self, content) :
		self.frigo.add_in_fridge(content)

	# TODO make this method private
	def add_frigo(self, content) :
		self.frigo.add_in_fridge(content)

	def remove_frigo(self, content) :
		self.frigo.remove_ingredient(content)

	def remove_list_from_fridge(self, content) :
		self.frigo.remove_list_ingredients(content)

	def add_ingredients_fridge(self, ingredients_to_add):

		for ingredient in ingredients_to_add:
			if not (ingredient in self.frigo.get_content()):
				self.frigo.add_in_fridge(ingredient)

	"""			getters 			"""
	def get_preferences(self) :
		return self.preferences

	def get_allergies(self) :
		return self.allergies

	def get_history(self) :
		return self.history

	def get_user_id(self) :
		return self.user_id

	def get_fridge(self) :
		return self.frigo.get_content()


if __name__ == "__main__" :
	usr = User(675719)
	print(usr.get_fridge())
	print(usr.get_allergies())
	print(usr.get_preferences())
	print(usr.get_history())
