import pandas as pd

import os
import sys
sys.path.append("..")
package_dir = os.path.dirname(os.path.abspath(__file__))
the_file = os.path.join(package_dir, '../Res/clean_reviews.csv')

def rateRecipe(userID, recipeId, note):
	scores = pd.read_csv(the_file)
	#print(userID + "\n")
	#print(recipeId)
	df = scores[(scores['profileID'] == int(userID)) & (scores['RecipeID'] == int(recipeId))]
	#print(df)
	if not(df.empty):
		scores.loc[(scores['RecipeID'] == int(recipeId)) & (scores['profileID'] == int(userID)), 'Rate'] = float(note)
	else:
		scores = scores.append(pd.DataFrame({ "RecipeID" : [int(recipeId)] , "profileID" : [int(userID)] , "Rate" : [float(note)] }, columns = ["RecipeID","profileID","Rate"]), sort = False)
	#pd.DataFrame(scores).to_csv("../Res/clean_reviews.csv", index = False)
	pd.DataFrame(scores).to_csv(the_file, index=False)
	#print("done")
	return 1

def getRate(userID, recipeID):
	#scores = pd.read_csv('../Res/clean_reviews.csv')
	scores = pd.read_csv(the_file)
	df = scores[(scores['profileID'] == int(userID)) & (scores['RecipeID'] == int(recipeID))]
	return df['Rate'][0]