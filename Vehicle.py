import json


class Vehicle:

    def __init__(self, regist_num, product_year, isPassenger, vehicle_mass):
        self.registration_number = regist_num
        self.year_of_production = product_year
        self.passenger = isPassenger
        self.mass = vehicle_mass

    def jsonEncoder(car):
        if isinstance(car, Vehicle):
            return car.__dict__
        else:
            raise TypeError(car.__class__.__name__ + "is not JSON seriazable")

    def getRegist_num(self):
        return self.registration_number

    def getProduct_year(self):
        return self.year_of_production

    def isPassenger(self):
        return self.passenger

    def getVehicle_mass(self):
        return self.mass
