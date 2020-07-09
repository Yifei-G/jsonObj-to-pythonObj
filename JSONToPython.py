from Vehicle import Vehicle
import json


def jsonTOPython(jsonData):
    try:
        # new_car will be a python dict variable.
        # Converting it to Vehicle object
        new_carJSON = json.loads(jsonData)
        # TODO: evaluating each key-value pairs of the dict is the data are
        # valid to be parsed as a Python object
        try:
            regist_num = new_carJSON["registration_number"]
            assert (regist_num.isalnum()) and (len(regist_num) == 8)
        except ValueError:
            print("Registration number is not valid!!")
            exit(1)

        try:
            product_year = new_carJSON["year_of_production"]
            assert (product_year.isdigit()) and (len(product_year) == 4)
        except AssertionError:
            print("The year of production is not in the valid format")
            exit(2)

        try:
            isPassenger = new_carJSON["passenger"]
            assert (isPassenger == True) or (isPassenger == False)
        except AssertionError:
            print("The Passenger can be only True or False!!")
            exit(3)

        try:
            vehicle_mass = new_carJSON["mass"]
            assert vehicle_mass > 900
        except ValueError:
            print("You didn't enter a numeric value")
            exit(4)
        except AssertionError:
            print("Opss your vehicle is so light!!")
            exit(4)

        new_car = Vehicle(regist_num, product_year, isPassenger, vehicle_mass)
        print("This is the car information:")
        print("Registration number:", new_car.getRegist_num())
        print("Year of production:", new_car.getProduct_year())
        print("Passenger:", new_car.isPassenger())
        print("Mass:", new_car.getVehicle_mass())

    except json.JSONDecodeError:
        print("Can't convert JSON object to Python object!")
