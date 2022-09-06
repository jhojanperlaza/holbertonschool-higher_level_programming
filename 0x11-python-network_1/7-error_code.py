#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays
the body of the response."""

import requests
import sys

if __name__ == "__main__":
    try:
        rq = requests.get(sys.argv[1])
        print(rq.status_code)
    except:
        print(rq.status_code)
