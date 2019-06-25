# LE DOSSIER SOTA EST DANS LE REPO : Recommendation-System-Q   (ici même)
https://github.com/PNS-PS7-1819/Recommendation-System-Q

# Recommendation-System-Q
Service for recommendation system implemented in Python.

# The repository contains 5 directories :

## Src :
	contains recommendation system source files.

## Test :
	contains functions tests.

## Res :
	contains data base files.

## Utilities :
	contains util functions used in the recommendation system

## SOTA :
	contains state of the art files


# Recommendation system work

## Collaborative filtering :
	It is based on collaborative filtering, using Python's library "Surprise".

	### Recommendation for individual user :
	Giving a users in parameter, it uses his history in order to retrieve his tried recipes.
	Then, it retrieves similar profiles in order to get their tried recipes, and predict the recipe's rating that would be given by the user.
	Finally, it filter the recommended recipes by user's preferences and allergies.

	### Recommendation for a group of users :
	Giving a group of users in parameter, it uses their history in order to retrieve their tried recipes.
	Then, it retrieves similar profiles in order to get their tried recipes, and predict the recipe's rating that would be given by them.
	Finally, it filter the recommended recipes by every user's preferences and allergies.

	### Configurable recommendation system :
	This recommendation ststem is configurable by users numbers: individual/groups, also by context : family, friends group.

# Tests and Quality

## Quality Test
In the file unit_test_CF_rec_test.py, we have a quality test that for given inputs, it execute several algorithms and checks that our system recommendation's failure score is the lowest.

## Tests
unit_test_db_reader.py tests the database reader file.
test_aggregated_voting tests the aggregated voting file.



# API roots
/getRecommendation : root to get recommendation, it is a POST request and takes list of users_id as arguments
/hey : test root, it returns a simple string
/helloWorld : test root, it tests JSON object use

# Server information
host : host='127.0.0.1'
port : port=81