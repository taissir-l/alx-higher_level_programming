#!/usr/bin/python3
"""The square module"""


class Square:
    """Class to create the square."""

    def __init__(self, size=0):
        """Size to private instance variabl setting

        Args:
            size: the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """to get the area od square

        Args:
            None

        Returns:
            Area
        """
        return (self.__size * self.__size)
