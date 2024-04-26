#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    h = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(h.text)))
    print("\t- content: {}".format(h.text))

