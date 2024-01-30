#!/usr/bin/python3
"""
Module 0-add_integer
A sum function

"""


def add_integer(a, b=98):
    """
    funcrion that returns sum of a and b

    Args:
        a (int): first int
        b (int): second int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
