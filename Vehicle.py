import json


class Vehicle:

    def __init__(self, regist_num, product_year, isPassenger, vehicle_mass):
        self.regist_num = regist_num
        self.product_year = product_year
        self.passenger = isPassenger
        self.vehicle_mass = vehicle_mass

    def jsonEncoder(car):
        if isinstance(car, Vehicle):
            return car.__dict__
        else:
            raise TypeError(car.__class__.__name__ + "is not JSON seriazable")
