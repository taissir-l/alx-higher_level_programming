#!/usr/bin/python3
"""module represented by a JSON string"""
import json


def from_json_string(my_str):
    """json string to python data structure"""
    return (json.loads(my_str))
