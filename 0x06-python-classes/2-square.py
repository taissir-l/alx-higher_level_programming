#!/usr/bin/python3
"""The square module continue"""


class Square:
    """Class to create the square."""

    def __init__(self, size=0):
        """size to private instance variable

        Args:
            size : square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
