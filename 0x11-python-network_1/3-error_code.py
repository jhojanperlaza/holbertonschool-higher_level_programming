#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)."""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)

    try:
        request.urlopen(req)
    except error.HTTPError as err:
        print(err.code)
