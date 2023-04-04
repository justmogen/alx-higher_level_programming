#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response

Usage: ./fetch_resquest_id.py <URL>

Argument:
    <URL>: the url to fetch

Returns:
    The value of the X-Request-Id variable
"""


import sys
import urllib.request

url = sys.argv[1]

requ = urllib.request.Request(url)

with urllib.request.urlopen(requ) as response:
    headers = response.headers
    request_id = headers.get('X-Request-Id')
    print(request_id)
