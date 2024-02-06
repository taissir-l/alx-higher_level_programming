#!/usr/bin/python3
"""json representation in a text file save"""
import json


def save_to_json_file(my_obj, filename):
    """function to save json to text file"""
    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
