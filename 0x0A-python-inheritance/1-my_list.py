#!/usr/bin/python3
"""Module inherited from the list class"""


class MyList(list):
    """class inherited from list"""
    def print_sorted(self):
        """prinnt sorted list"""
        print(sorted(self))
