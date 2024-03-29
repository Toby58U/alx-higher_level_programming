#!/usr/bin/python3
"""
Python script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    base_url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    res = get(base_url, auth=auth.HTTPBasicAuth(username, password))
    print(res.json().get('id'))
