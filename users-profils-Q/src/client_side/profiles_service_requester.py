from collections import OrderedDict

import src.user_profil as user_profil


'''''
 This method calls get_user_profil on WebService
 It returns a list of lists : list of preferences, list of allergies, list of fridge contained ingredients
 Parameters : user_id
 Exceptions : if user_id is not found, it prints error message and returns empty list
'''''
def get_user_profil(id) :

    complete_profil = [[],[], [], [], []]

    # get User
    try :
        user = user_profil.User_Profil(id)
        complete_profil[4] = 0  # 0 success code

        #if user.get_user_id() == None :
            #return []

        # get preferences, allergies and fridge
        preferences = user.get_preferences()
        allergies = user.get_allergies()
        fridge = user.get_fridge()
        history = user.get_history()

        # create complete profil
        '''complete_profil.append(preferences)
        complete_profil.append(allergies)
        complete_profil.append(fridge)
        complete_profil.append(history)'''
        #break
        complete_profil[0] = preferences
        complete_profil[1] = allergies
        complete_profil[2] = fridge
        complete_profil[3] = history

    except ValueError as exception :
        complete_profil[4] = -1  # -1 failure code
        print(exception)

    #l = len(complete_profil[0]) + len(complete_profil[1]) + len(complete_profil[2]) + len((complete_profil[3]))
    #print(l)
    #print(complete_profil)
    return complete_profil


'''''
 This method return group of users profiles to WebService
 It returns a list of lists : list of preferences, list of allergies, list of fridge contained ingredients
 Parameters : id_list: list of group user's ids
 Exceptions : if user_id is not found, it prints error message and returns empty list
'''''
def get_group_profils(id_list):

    complete_profils = [[],[], [], [], []]

    for id in id_list :
        try :
            one_profil = get_user_profil(id)

            if one_profil[4] == 0 :

                if ( len(one_profil[0]) > 0 and one_profil[0][0] != '' ) :
                    complete_profils[0] += one_profil[0]

                if ( len(one_profil[1]) > 0 and  one_profil[1][0] != '') :
                    complete_profils[1] += one_profil[1]

                if (len(one_profil[3]) > 0 and  one_profil[3][0] != ''):
                    complete_profils[3] += one_profil[3]
                    complete_profils[3] = list(OrderedDict.fromkeys(complete_profils[3]))

                if str(id) == str(id_list[0]) :
                    complete_profils[2] += one_profil[2]

                if complete_profils[4] != -1 :
                    complete_profils[4] = 0

            else :
                print("id = "+str(id) + " non trouve")
                complete_profils[4] = -1

        except ValueError as exception :
            complete_profils[4] = -1   # -1 failure code
            print(exception)

    return complete_profils
