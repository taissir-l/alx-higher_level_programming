#!/usr/bin/python3
"""class tconverter o json"""


def class_to_json(obj):
    """json class

    Args:
        obj: the class
    """
    return (obj.__dict__)
