#!usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.

Usage: ./6-post_email.py <url> <email>

"""


import sys
import requests


if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]
    dataload = {'email': email}

    req = requests.post(url, data=dataload)
    print(req.text)
