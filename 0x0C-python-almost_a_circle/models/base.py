#!/usr/bin/python3
"""
Module that defines the class Base
"""


import json
import csv


class Base():
    """constructor method
    Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that returns JSON string of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to a file"""
        objs = []
        if list_objs is not None:
            for x in list_objs:
                objs.append(cls.to_dictionary(x))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """function of the list of the JSON string of json_string"""
        if json_string is None:
            json_string = "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        lst = []
        with open(filename, "r") as f:
            instance = cls.from_json_string(f.read())
        for i, d in enumerate(instance):
            lst.append(cls.create(**instance[i]))
        return lst
