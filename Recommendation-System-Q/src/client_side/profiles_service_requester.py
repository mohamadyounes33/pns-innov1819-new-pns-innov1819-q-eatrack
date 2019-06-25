import zeep as zeep

# attributs
wsdl_url = "http://localhost:8733/Design_Time_Addresses/WcfServiceLibrary1/Service1/?wsdl"
client = zeep.Client(wsdl=wsdl_url)


# This method calls get_user_profil on WebService
# It returns a list of lists : list of preferences, list of allergies, list of fridge contained ingredients
# Parameters : user_id
def get_profil(id):
    id_str = str(id)
    return client.service.GetUserProfil(args=[id_str])


# return client.service.GetUserProfil(id_str)


# This method calls get_group_user_profil on WebService
# It returns a list of lists : list of preferences, list of allergies, list of fridge contained ingredients
# Parameters : id_list: list of group user's ids
def get_group_profils(id_list):
    if (len(id_list) != 0):
        args = "" + str(id_list[0])
        for i in range(1, len(id_list)):
            args += "," + str(id_list[i])

        return client.service.GetGroupUserProfil(args=str(args))

    return [[], [], [], [], []]


if __name__ == "__main__":
    print(get_profil(675719))
    print("-------------------------------------------------------------------")
    print(get_group_profils([675719, 1478626]))
    print("-------------------------------------------------------------------")
    print(get_group_profils([1478626, 675719]))
