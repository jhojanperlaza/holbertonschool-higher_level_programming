#!/usr/bin/python3
""" Python script that takes your GitHub
credentials (username and password) and
uses the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    basic = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    result_response =  requests.get('https://api.github.com/user', auth=basic)

    if result_response.status_code >= 400:
        print("None")
    else:
        print(result_response.json().get("id"))
