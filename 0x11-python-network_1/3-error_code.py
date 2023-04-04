#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body
of the reponse (decoded in utf-8).

Usage: ./fetch_resquest_id.py <URL>

Argument:
    <URL>: the url to fetch

Returns:
    The body of the response from the server (decoded in utf-8) or 
    an error message if an HTTP error occurs
"""


import sys
import urllib.request
import urllib.error

url = sys.argv[1]

try:
    with urllib.request.urlopen(requ) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
