#!/usr/bin/python3
"""class object serializer"""


class Student:
    """serializer"""

    def __init__(self, first_name, last_name, age):
        """function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of a Student"""
        return (self.__dict__)
