from Vehicle import Vehicle
import json


def jsonTOPython(jsonData):
    try:
        # new_car will be a python dict variable.
        # Converting it to Vehicle object
        new_car = json.loads(jsonData)

        # TODO: evaluating each key-value pairs of the dict is the data are
        # valid to be parsed as a Python object
    except json.JSONDecodeError:
        print("Can't convert JSON object to Python object!")
