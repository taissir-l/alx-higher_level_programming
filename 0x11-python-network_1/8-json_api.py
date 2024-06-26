#!/usr/bin/python3
"""sends request to URL with a letter
"""

import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = ""
    payload = {'q': query}
    r = requests.post(url, data=payload)

    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
