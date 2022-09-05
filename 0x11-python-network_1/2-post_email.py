#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable
found in the header of the response."""

from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = parse.urlencode(values)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
