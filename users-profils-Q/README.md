# users-profils-Q
A server to manage users profils accessing a dedicated database and providing an API to make CRUD requests 

# The repository contains 2 directories :

## Src :
	contains source to manage profiels database

## Res :
	contains data base files.

## root directory :
    contains server file "__init__.py" 
    
## Test :
    contains tests


# API roots
/inquirePreferences : root to add a list of preferences to the profile's row in database file.
/inquireAllergies : root to add a list of allergies to the profile's row in database file.
/removePreferences : root to remove a list of preferences from the profile's row in database file.
/removeAllergies : root to remove a list of allergies from the profile's row in database file.
/addToFridge : root to add a list of ingredients to the profile's row in database file.
/removeFromFridge : root to remove a list of ingredients from the profile's row in database file.
/emptyFridge : root to remove all the ingredients from the profile's row in database file.
/getUserProfil : root to get all the profile's data from database file.
/getGroupUserProfil : root to get all the profile's data of the group members from database file.
/evaluateRecipe : root to rate a recipe

# Server information
host : host='127.0.0.1'
port : port=81