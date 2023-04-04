#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response.

Usage: ./7-error_code.py http://0.0.0.0:5000

"""


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
