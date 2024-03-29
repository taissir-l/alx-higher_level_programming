#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        x = fct(*args)
        return (x)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
