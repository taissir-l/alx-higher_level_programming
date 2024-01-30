#!/usr/bin/python3
"""
Module 6-max_integer.py
max integer

"""


def max_integer(list=[]):
    """function to find and return the max integer in a list of integers, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    j = 1
    while j < len(list):
        if list[j] > result:
            result = list[j]
        j += 1
    return result
