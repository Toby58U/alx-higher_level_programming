#!/usr/bin/python3
"""
Takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
(handling HTTP errors)
"""
from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
