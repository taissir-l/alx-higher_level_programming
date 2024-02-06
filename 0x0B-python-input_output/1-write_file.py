#!/usr/bin/python3
"""overwrite byte content"""


def write_file(filename="", text=""):
    """function to write to file"""
    with open(filename, 'w', encoding="utf-8") as myfile:
        return (myfile.write(text))
