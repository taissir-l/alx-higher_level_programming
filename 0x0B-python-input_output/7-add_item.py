#!/usr/bin/python3
"""module to add all argumenst to a json file"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f = 'add_item.json'

if __name__ == "__main__":
    try:
        save_to_json_file(load_from_json_file(f) + argv[1:], f)
    except (FileNotFoundError, ValueError):
        save_to_json_file(argv[1:], f)
