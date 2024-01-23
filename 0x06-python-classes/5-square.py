#!/usr/bin/python3
"""The square module"""


class Square:
    """The class create square."""

    def __init__(self, size=0):
        """private instance variable setter

        Args:
            size (int): square size
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
            Area (int)
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """gets size of the  variable"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """value of the size

        Args:
            value: reset value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """shows the square form the size"""
        value = self.__size
        for i in range(value):
            [print('#', end='') for j in range(value)]
            print('')
        if value == 0:
            print('')
