#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""

if __name__ == '__main__':
    from requests import post
    from sys import argv

    base_url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    res = post(base_url, data)

    type_res = res.headers['content-type']

    if type_res == 'application/json':
        result = res.json()
        _id = result.get('id')
        name = result.get('name')
        if (result != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
