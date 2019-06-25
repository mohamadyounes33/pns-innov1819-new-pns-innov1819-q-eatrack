import csv

import pandas as pd

import os

package_dir = os.path.dirname(os.path.abspath(__file__))
resource_file_path = os.path.join(package_dir,'../Res/fridge_content.csv')
ingredients_file_path = os.path.join(package_dir,'../Res/ingredients.csv')

# function that returns user's fridge content stored in data base csv file
# parameters : user_id : integer (user's id)
# return : list of ingredient contained in fridge
def get_fridge_content(user_id):
    with open(resource_file_path, 'r') as profiles:
        reader = csv.reader(profiles, delimiter=';')
        for row in reader:
            if (str(row[0]) == str(user_id)):
                if len(row[1]) == 0:
                    return []
                else:
                    return row[1].split(',')
        return []


def addInFile(user, resource, section, item_to_add):
    profiles = pd.read_csv(resource, sep=";")

    df = profiles[(profiles['user_id'] == int(user.user_id))]

    if not (df.empty):

        already_content = df[section].values.tolist()

        if (not (type(already_content[0]) is float)):
            already_content = already_content[0].split(",")
        else:
            already_content = []

        for item in item_to_add:
            if not (item in already_content):
                already_content.append(item)
        # print(already_content)
        new_section_content = ','.join(map(str, already_content))

        profiles.loc[(profiles['user_id'] == int(user.user_id)), section] = new_section_content

    else:  # useer id doesn't exist already
        new_row_map = {}
        new_row_map['user_id'] = [int(user.user_id)]

        item_to_add_string = ""
        for item in item_to_add:
            item_to_add_string += str(item)
            item_to_add_string += ","
        item_to_add_string = item_to_add_string[:-1]

        new_row_map[section] = [item_to_add_string]
        zabi = []
        zabi.append("user_id")
        #print("section = ", section)
        x = section
        zabi.append(x)
        #print("zabi : ", zabi)
        #print("--------")
        #print("dict : ")
        #print(new_row_map)
       # print(pd.DataFrame(new_row_map, columns=zabi))
        #print("----")
        #print(profiles)
        #print("---second")
        profiles = profiles.append(pd.DataFrame(new_row_map), sort=False)
        #print(profiles)

    pd.DataFrame(profiles).to_csv(resource, sep=";", index=False)

        #print("--_____----" + item_to_add_string)




def removeInFile(user, resource, section, item_to_remove):
    profiles = pd.read_csv(resource, sep=";")

    df = profiles[(profiles['user_id'] == int(user.user_id))]
    already_content = df[section].values.tolist()

    if (len(item_to_remove) != 0 and not(df.empty) ):
        already_content = already_content[0].split(",")
    else:
        return
    if not (df.empty):

        for item in item_to_remove:
            if item in already_content:
                already_content.remove(item)
        # print(already_content)
        new_section_content = ','.join(map(str, already_content))

        profiles.loc[(profiles['user_id'] == int(user.user_id)), section] = new_section_content

    pd.DataFrame(profiles).to_csv(resource, sep=";", index=False)

def checkIfIngredientsExist(ingredients) :

    ingredientsExistant = pd.read_csv(ingredients_file_path)
    #df = ingredientsExistant[(ingredientsExistant['ingredient'] in ingredients)]

    res = [[],[]]
    for i in range(len(ingredients)) :
        df = ingredientsExistant[(ingredientsExistant['ingredient'] == ingredients[i])]
        if df['ingredient'].isin([ingredients[i]]).any() : 
            #print(str(ingredients[i]) + " is in ingredients")
            #print("#######")
            #print(df['ingredient'])
            #print("#######")
            res[0].append(ingredients[i])
        else :
            #print(str(ingredients[i]) + " is not in ingredients")
            res[1].append(ingredients[i])
    return res
    
if __name__ == '__main__' :
    print(get_fridge_content(675719))
    print(checkIfIngredientsExist(["Bloody Mary mix","Blue Curacao", "salut"]))
