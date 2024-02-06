#!/usr/bin/python3
"""class to read element from the file"""


def read_file(filename=""):
    """read element to the file"""
    with open(filename, encoding="utf-8") as myfile:
        line = myfile.readlines()
        for i in line:
            print(i, end='')
