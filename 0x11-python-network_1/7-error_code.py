#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays
the body of the response."""

import requests
import sys

if __name__ == "__main__":
    rquest = requests.get(sys.argv[1])
    if rquest.status_code >= 400:
        print("Error code: {}".format(rquest.status_code))
    else:
        print(rquest.text)
