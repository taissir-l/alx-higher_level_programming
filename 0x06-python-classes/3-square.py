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
