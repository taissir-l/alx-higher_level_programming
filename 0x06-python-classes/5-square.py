#!/usr/bin/python3
"""ceates aSquare and set the size as private instance variable"""


class Square:
    """class to create a square."""

    def __init__(self, size):
        """the initialzing size to piV

        Args:
            size (int): the square size
        """
        self.__size = size

     def area(self):
        """get the square area

        Args:
            None

        Returns:
            square area
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """gets size variable"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size to value

        Args:
            value: value reset
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
