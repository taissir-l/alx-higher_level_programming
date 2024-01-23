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
