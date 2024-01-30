#!/usr/bin/python3
"""
Module 5-text_indentation
inserts two lines afetr every occurence of specific char

"""


def text_indentation(text):
    """function that inserts two lines afetr `.`, `?`, and `:`."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")


    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1


    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
