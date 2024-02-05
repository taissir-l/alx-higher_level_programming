#!/usr/bin/python3
"""object is an instance of a class that inherited
from the specified class"""


def inherits_from(obj, a_class):
    """ifunctin that check if it inherited instance of that class"""
    return isinstance(obj, a_class) and type(obj) != a_class
