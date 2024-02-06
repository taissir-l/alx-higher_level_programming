#!/usr/bin/python3
"""class file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """text after each line containing a given string in a file"""
    x = ""
    with open(filename) as r:
        for line in r:
            x += line
            if search_string in line:
                x += new_string
    with open(filename, "w") as w:
        w.write(x)
