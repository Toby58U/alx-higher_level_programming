#!/usr/bin/python3
"""
Sends a request to the URL and
displays:
- The body of the response if there are no errors
- The error code when there is an HTTP error.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
