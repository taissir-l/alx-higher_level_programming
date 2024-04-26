#!/usr/bin/python3
"""script thst sends a request to URL of the X-Request-Id
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
