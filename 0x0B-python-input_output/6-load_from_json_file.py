#!/usr/bin/python31
"""json load file string"""
import json


def load_from_json_file(filename):
    """function to load py data structure from file"""
    with open(filename, 'r') as myfile:
        return (json.load(myfile))
