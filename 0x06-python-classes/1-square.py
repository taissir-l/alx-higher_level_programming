#!/usr/bin/python3
"""defines a quare and set the size as private instance variable"""


class Square:
    """class to create square."""

    def __init__(self, size):
        """the Initialzation of the size to piV

        Args:
            size (int): the square size
        """

        self.__size = size
