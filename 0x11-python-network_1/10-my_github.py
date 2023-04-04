#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and password) and uses
the GitHub API to display the user ID.

"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, passwd))
    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print(None)
