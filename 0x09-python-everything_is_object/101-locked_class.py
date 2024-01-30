#!/usr/bin/python3
"""locked class"""


class LockedClass:
    """
    function that only allows instatiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
