#!/usr/bin/python3
"""square module"""


class Square:
    """Class to create the square."""

    def __init__(self, size=0):
        """size for private instance variable

        Args:
            size : square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of the square

        Args:
            None

        Returns:
            Area of square
        """
        return (self.__size * self.__size)


    @property
    def size(self):
        """gets size variable"""
        return (self.__size)


    @size.setter
    def size(self, value):
        """size of value

        Args:
            value: to reset
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
