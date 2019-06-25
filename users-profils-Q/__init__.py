'''
	This program is an API to manage user profiles and provides API for CRUD requests
'''

from flask import Flask, request, jsonify

from src import user_profil as user_profil
from src.client_side import profiles_service_requester
from src.evaluationRecipe import rateRecipe

app = Flask(__name__)


# test root
@app.route("/hey", methods=['GET', 'POST'])
def gethey():
    return ("hey hey hey");



# root to add list of preferences
@app.route("/inquirePreferences", methods=['POST'])
def inquirePreferences():

	input = request.json
	userID = input['userID']
	preferences = input['preferences']
	print("################")
	print("User " + str(userID) + " inquire his preferences : " + str(preferences) +"\n")
	print("################")

	try:
		user = user_profil.User_Profil(userID)
	except:
		tmp = {}
		tmp["status"] = "User not found"
		res = jsonify(tmp)
		return str(res.json)

	res = user.add_preference(preferences)

	for preference in user.get_preferences() :
		print("_________ "+str(preference))

	tmp = {}
	tmp["status"] = "Preferences have been added to the user."
	tmp["preferences"] = user.get_preferences()
	tmp["added"] = res[0]
	tmp["already inquired"] = res[1]
	tmp["Unknown"] = res[2]
	res = jsonify(tmp)
	return str(res.json)




# root to add a list of allergies
@app.route("/inquireAllergies", methods=['POST'])
def inquireAllergies():

	input = request.json
	userID = input['userID']
	allergies = input['allergies']
	print("################")
	print("User " + str(userID) + " inquire his allergies : " + str(allergies) +"\n")
	print("################")

	try:
		user = user_profil.User_Profil(userID)
	except:
		tmp = {}
		tmp["status"] = "User not found"
		res = jsonify(tmp)
		return str(res.json)

	res = user.add_allergies(allergies)


	for allergie in user.get_allergies() :
		print("_________ "+str(allergie))

	tmp = {}
	tmp["status"] = "Preferences have been added to the user."
	tmp["allergies"] = user.get_allergies()
	tmp["added"] = res[0]
	tmp["already inquired"] = res[1]
	tmp["Unknown"] = res[2]
	res = jsonify(tmp)
	return str(res.json)



# root to remove a list of preferences
@app.route("/removePreferences", methods=['POST'])
def removePreferences():

	input = request.json
	userID = input['userID']
	preferences = input['preferences']
	print("################")
	print("User " + str(userID) + " removed " + str(preferences) + " to his preferences\n")
	print("################")
	
	try:
		user = user_profil.User_Profil(userID)
	except:
		tmp = {}
		tmp["status"] = "User not found"
		res = jsonify(tmp)
		return str(res.json)
		
	res = user.remove_preferences(preferences)
	
	for preference in user.get_preferences() :
		print("_________ "+str(preference))

	tmp = {}
	tmp["status"] = "Preferences :  " + str(preferences) +" have been removed from the user's preferences"
	tmp["preferences"] = user.get_preferences()
	tmp["removed"] = res[0]
	tmp["Was not in preferences"] = res[1]
	tmp["Unknown"] = res[2]
	res = jsonify(tmp)
	return str(res.json)



# root to remove a list of allergies
@app.route("/removeAllergies", methods=['POST'])
def removeAllergies():

	input = request.json
	userID = input['userID']
	allergies = input['allergies']
	print("################")
	print("User " + str(userID) + " removed " + str(allergies) + " to his allergies\n")
	print("################")
	
	try:
		user = user_profil.User_Profil(userID)
	except:
		tmp = {}
		tmp["status"] = "User not found"
		res = jsonify(tmp)
		return str(res.json)

	res = user.remove_allergies(allergies)

	for allergie in user.get_allergies() :
		print("_________ "+str(allergie))

	tmp = {}
	tmp["status"] = "Ingredient " + str(allergies) +" have been removed from the user allergies"
	tmp["allergies"] = user.get_allergies()
	tmp["removed"] = res[0]
	tmp["Was not in allergies"] = res[1]
	tmp["Unknown"] = res[2]
	res = jsonify(tmp)
	return str(res.json)


# root to add a list of ingredients to the frigo
@app.route("/addToFridge", methods=['POST'])
def addIngredientsFrigo():
	input = request.json
	userID = input['userID']
	ingredients = input['items']   #list of ingredients
	print("################")
	print("User " + str(userID) + " added " + str(ingredients) + " to his frigo\n")
	print("################")

	try:
		user = user_profil.User_Profil(userID)
	except:
		tmp = {}
		tmp["status"] = "User not found"
		res = jsonify(tmp)
		return str(res.json)
	

	res = user.add_ingredients_fridge(ingredients)

	for ingredient in user.get_fridge():
		print("_________ " + str(ingredient))

	tmp = {}
	tmp["status"] = "Ingredient " + str(ingredients) + " have been added to the user fridge"
	tmp["fridge"] = user.get_fridge()
	tmp["added"] = res[0]
	tmp["already in fridge"] = res[1]
	tmp["Unknown"] = res[2]
	res = jsonify(tmp)
	return str(res.json)


# root to add a list of ingredients to the frigo
@app.route("/removeFromFridge", methods=['POST'])
def removeIngredientsFrigo():
	input = request.json
	userID = input['userID']
	ingredients = input['items']   #list of ingredients
	print("################")
	print("User " + str(userID) + " removed " + str(ingredients) + " from his frigo\n")
	print("################")

	try:
		user = user_profil.User_Profil(userID)
	except:
		tmp = {}
		tmp["status"] = "User not found"
		res = jsonify(tmp)
		return str(res.json)

	res = user.remove_ingredients_fridge(ingredients)

	for ingredient in user.get_fridge():
		print("_________ " + str(ingredient))

	tmp = {}
	tmp["status"] = "Ingredient " + str(ingredients) + " have been removed from the user fridge"
	tmp["fridge"] = user.get_fridge()
	tmp["removed"] = res[0]
	tmp["Was not in fridge"] = res[1]
	tmp["Unknown"] = res[2]
	res = jsonify(tmp)
	return str(res.json)


@app.route("/emptyFridge", methods=['POST'])
def removeAllIngredientsFrigo():
	input = request.json
	userID = input['userID']
	print("################")
	print("User " + str(userID) + " cleared his fridge\n")
	print("################")

	try:
		user = user_profil.User_Profil(userID)
	except:
		tmp = {}
		tmp["status"] = "User not found"
		res = jsonify(tmp)
		return str(res.json)

	cleared_fridge = user.clear_fridge()

	for ingredient in user.get_fridge():
		print("_________ " + str(ingredient))

	tmp = {}
	tmp["status"] = "user's fridge has "+ str(len(cleared_fridge)) + " ingredients in his gridge\n"
	tmp["fridge"] = user.get_fridge()
	res = jsonify(tmp)
	return str(res.json)

@app.route("/getUserProfil", methods=['POST'])
def getUserProfil():
	input = request.json
	userID = input['userID']
	print("################")
	print("Get user " + str(userID) + " data\n")
	print("################")

	result = profiles_service_requester.get_user_profil(userID)
	res = {}
	res['preferences'] = result[0]
	res['allergies'] = result[1]
	res['fridge'] = result[2]
	res['history'] = result[3]
	res['status'] = result[4]
	tmp = jsonify(res)
	print(str(tmp))


	return str(tmp.json)

# return a list of list, each one containing : the user's preferences, the user's allergies, the user's fridge, the user's history and a return status code 
@app.route("/getGroupUserProfil", methods=['POST'])
def getGroupUserProfil():
	input = request.json
	userIDs = input['userID']

	print("################")
	print("Get user " + str(userIDs) + " data\n")
	print("################")

	result = profiles_service_requester.get_group_profils(userIDs)
	res = {}
	res["preferences"] = result[0]
	res["allergies"] = result[1]
	res["fridge"] = result[2]
	res["history"] = result[3]
	res["status"] = result[4]
	tmp = jsonify(res)
	print(str(tmp.json))
	return str(tmp.json)

@app.route("/getUserFridge/<id>", methods=['GET'])
def getUserFridge(id):

	print("################")
	print("Get user " + str(id) + " fridge\n")
	print("################")
	res = {}
	try:
		user = user_profil.User_Profil(id)
		res["fridge"] = user.get_fridge()
		return jsonify(res)
	except:
		res["fridge"] = []
		return jsonify(res)

@app.route("/evaluateRecipe", methods=['POST'])
def evaluateRecipe():

	input = request.json
	userID = input['userID']
	recipeID = input['recipeID']
	note = input['rate']
	print("################")
	print("User " + str(userID) + " evaluate recipe " + str(recipeID) + " with note : " + str(note) + "\n")
	print("################")
	rateRecipe(userID, recipeID, note)
	tmp = {}
	tmp["status"] = 1
	res = jsonify(tmp)
	return str(res.json)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


