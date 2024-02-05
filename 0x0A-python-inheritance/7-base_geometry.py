#!/usr/bin/python3
"""base geometry class BaseGeometry"""


class BaseGeometry:
    """base geometry"""

    def area(self):
        """new method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
