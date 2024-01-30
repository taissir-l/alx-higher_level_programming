#!/usr/bin/python3
"""
Module 4-print_square
function to print a square

"""


def print_square(size):
    """
    function that prints square with character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        print("\n".join(["#" * size for i in range(size)]))
