#!/usr/bin/python3
""" script that sends a request to a URL and displays the
value of the X-Request-Id
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    h = requests.get(url)
    print(h.headers.get("X-Request-Id"))
