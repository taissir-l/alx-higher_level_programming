#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """to append to the file

    Args:
        filename: filename
        text: to append

    Returns:
        bytes number
    """
    with open(filename, 'a', encoding="utf-8") as myfile:
        return (myfile.write(text))
