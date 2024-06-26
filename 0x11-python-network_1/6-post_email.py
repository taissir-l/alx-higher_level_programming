#!/usr/bin/python3
"""URL that POST request to a given URL
"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        form_data = [('email', email)]
        response = requests.post(url, data=form_data)
        print(response.text)
