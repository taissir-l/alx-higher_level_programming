#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """exchange operators == and !="""

    def __eq__(self, value):
        """exchange == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """exchange != operator with == behavior"""
        return self.real == value
