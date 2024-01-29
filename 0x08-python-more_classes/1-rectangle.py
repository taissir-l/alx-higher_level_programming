#!/usr/bin/python3
"""class that represents a rectangle"""


class Rectangle:
    """a rectangle"""

    def __init__(self, width=0, height=0):
        """ rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: not integer
            ValueError: less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """brings attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """takes attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """gets attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
