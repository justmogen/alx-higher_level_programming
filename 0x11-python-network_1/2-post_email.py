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
import urllib.parse

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
requ = urllib.request.Request(url, data)

with urllib.request.urlopen(requ) as response:
    body = response.read().decode('utf-8')
    print(body)
