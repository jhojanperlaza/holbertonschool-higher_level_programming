#!/usr/bin/python3
""" Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""

from requests import post
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""

    if len(sys.argv) == 2:
        q = sys.argv[1]

    value = {'q': q}
    rq = post(url, data=value)

    try:
        j_son = rq.json()
        if j_son.isEmpty():
            print("No result")
        else:
            print("[{}] {}".format(j_son.get("id"), j_son.get("name")))
    except Exception:
        print("Not a valid JSON")
