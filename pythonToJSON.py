from Vehicle import Vehicle
import json


def dataToJSON():
    try:
        regist_num = input(
            "Registration number (combined with letter and numbers, 8 characters!):")
        assert (regist_num.isalnum()) and (len(regist_num) == 8)
    except ValueError:
        print("You didn't enter a valid Registration number")
        exit(1)
    except AssertionError:
        print("The Registration number is not in a valid format!")
        exit(1)

    try:
        product_year = input("Year of production:")
        assert (product_year.isdigit()) and (len(product_year) == 4)
    except AssertionError:
        print("The year of production is not in the valid format")
        exit(2)

    try:
        isPassenger = input("Passenger[y/n]:")
        assert (isPassenger == "y") or (isPassenger == "n")
        if isPassenger == "y":
            isPassenger = True
        else:
            isPassenger = False
    except AssertionError:
        print("The Passenger can only be y or n!!!")
        exit(3)

    try:
        vehicle_mass = float(input("Vehicle mass: (at least 900):"))
        assert vehicle_mass > 900

    except ValueError:
        print("You didn't enter a numeric value")
        exit(4)
    except AssertionError:
        print("Opss your vehicle is so light!!")
        exit(4)

    new_car = Vehicle(regist_num, product_year, isPassenger, vehicle_mass)
    new_carJSON = json.dumps(new_car, default=Vehicle.jsonEncoder)
    print(new_carJSON)
