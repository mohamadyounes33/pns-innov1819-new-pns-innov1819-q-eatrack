'''
	This program is an API to communicate with recommendation system
	Root 1 : /getRecommendation is a POST request. It receives a JSON object in argument with user's preferences and allergies.
	It returns a JSON Object with recipes to be recommended
'''

from flask import Flask, request, jsonify

from src import user as db_reader
from src.group_recommender import aggregated_voting

app = Flask(__name__)


# @app.route("/helloWorld/<uuid>", methods=['GET','POST'])
# def index() :
#	content = request.get_json(silent=True)
#	return(json.dumps({"name": request.args.get('name'), "age": request.args.get('age')}))

@app.route("/hey", methods=['POST'])
def gethey():
    return ("hey hey hey");


@app.route("/helloWorld", methods=['POST'])
def getHelloWorld():

		tmp = {}
		tmp["message"] = "hello world!"
		tmp["a"] = "b"
		res = jsonify(tmp)
		print("log ################")
		print(res)
		print("log ################")
		return str(res.json)





@app.route("/inquirePreferences", methods=['POST'])
def inquirePreferences():

	input = request.json
	userID = input['userID']
	preferences = input['preferences']
	print("################")
	print("User " + str(userID) + " inquire his preferences : " + str(preferences) +"\n")
	print("################")

	user = db_reader.User(userID)

	user.add_preference(preferences)


	for preference in user.get_preferences() :
		print("_________ "+str(preference))

	tmp = {}
	tmp["status"] = "Preferences have been added to the user."
	tmp["preferences"] = user.get_preferences()
	res = jsonify(tmp)
	return str(res.json)




@app.route("/inquireAllergies", methods=['POST'])
def inquireAllergies():

	input = request.json
	userID = input['userID']
	allergies = input['allergies']
	print("################")
	print("User " + str(userID) + " inquire his allergies : " + str(allergies) +"\n")
	print("################")

	user = db_reader.User(userID)

	user.add_allergies(allergies)


	for allergie in user.get_allergies() :
		print("_________ "+str(allergie))

	tmp = {}
	tmp["status"] = "Preferences have been added to the user."
	tmp["allergies"] = user.get_allergies()
	res = jsonify(tmp)
	return str(res.json)




@app.route("/removePreferences", methods=['POST'])
def removePreferences():

	input = request.json
	userID = input['userID']
	preferences = input['preferences']
	print("################")
	print("User " + str(userID) + " removed " + str(preferences) + " to his preferences\n")
	print("################")
	
	user = db_reader.User(userID)
	user.remove_preferences(preferences)
	
	for preference in user.get_preferences() :
		print("_________ "+str(preference))

	tmp = {}
	tmp["status"] = "Ingredient " + str(preferences) +" have been removed from the user's preferences"
	tmp["preferences"] = user.get_preferences()
	res = jsonify(tmp)
	return str(res.json)



@app.route("/removeAllergies", methods=['POST'])
def removeAllergies():

	input = request.json
	userID = input['userID']
	allergies = input['allergies']
	print("################")
	print("User " + str(userID) + " removed " + str(allergies) + " to his allergies\n")
	print("################")
	
	user = db_reader.User(userID)

	user.remove_allergies(allergies)

	for allergie in user.get_allergies() :
		print("_________ "+str(allergie))

	tmp = {}
	tmp["status"] = "Ingredient " + str(allergies) +" have been removed from the user allergies"
	tmp["allergies"] = user.get_allergies()
	res = jsonify(tmp)
	return str(res.json)


@app.route("/getRecommendation", methods=['POST', 'GET'])
def getRecommendation():

	input = request.json
	users = input['users']
	users = [int(i) for i in users]

	try:
		if(input['fridge'] == "True"):
			res = aggregated_voting(users, True)
			for x in res:
				x["Recipe Name"] = x["Recipe Name"].replace('\"', '')
				x["Recipe Name"] = x["Recipe Name"].replace('\'', '')
				x["Ingredients"] = x["Ingredients"].replace('\"', '')
				x["Ingredients"] = x["Ingredients"].replace('\'', '')
				x["Directions"] = x["Directions"].replace('\"', '')
				x["Directions"] = x["Directions"].replace('\'', '')
			print(len(res))
			return str(res)
		else:
			res = aggregated_voting(users)
			for x in res:
				x["Recipe Name"] = x["Recipe Name"].replace('\"', '')
				x["Recipe Name"] = x["Recipe Name"].replace('\'', '')
				x["Ingredients"] = x["Ingredients"].replace('\"', '')
				x["Ingredients"] = x["Ingredients"].replace('\'', '')
				x["Directions"] = x["Directions"].replace('\"', '')
				x["Directions"] = x["Directions"].replace('\'', '')
			print(len(res))
			return str(res)
	except ValueError as exceptionn :
		print(exceptionn)
		tmp = {}
		tmp["status"] = "An user is unknown by the system"
		res = jsonify(tmp)
		return str(res.json)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8282, debug=True)