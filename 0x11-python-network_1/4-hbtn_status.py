#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status using the
requests package and displays the body of the response.

Usage: ./fetch_alx_status.py

Returns:
    The body of the response from the server or
    an error message if the request fails
"""


import requests

if __name__ == "__main__":
    data = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(data.text)))
    print("\t- content: {}".format(data.text))
else:
    print("Request failed with status code {}".format(response.status_code))
