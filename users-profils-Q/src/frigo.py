'''
	This program represents user's fridge.
	It stores the fridge content : list of ingredients
'''

class Frigo :


	# attributs
	frigo_content = []

	# constructor
	def __init__(self, content) :
		self.frigo_content = content

	def add_in_fridge(self, ingredient) :
		self.frigo_content.append(ingredient)


	def get_fridge(self) :
		return self.frigo_content


	def clear_fridges(self) :
		self.frigo_content = []


	def remove_ingredient(self, ingredient) :
		if ingredient in self.frigo_content :
			self.frigo_content.remove(ingredient)

	def remove_list_ingredients(self, ingredients_list) :
		for ingredient in ingredients_list :
			self.remove_ingredient(ingredient)

	def get_content(self) :
		return self.frigo_content