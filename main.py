from pythonToJSON import dataToJSON
from JSONToPython import jsonTOPython


try:
    print("What can I do for you?")
    print("1 - produce a JSON string describing a vehicle")
    print("2- decode a JSON string into vehicle data")
    user_choice = input("Your choice:")
    assert (int(user_choice) == 1) or (int(user_choice) == 2)
    if int(user_choice) == 1:
        dataToJSON()
    else:
        jsonData = input("Enter vehicle JSON string:")
        jsonTOPython(jsonData)


except AssertionError:
    print("Invalid choise! please select the feature using number 1 or 2")
