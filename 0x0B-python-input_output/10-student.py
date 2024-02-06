#!/usr/bin/python3
"""class object serializer"""


class Student:
    """serializer"""

    def __init__(self, first_name, last_name, age):
        """function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """dictionary representation of a Student"""
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return (self.__dict__)
