#!/usr/bin/python3
""" Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""

from requests import post
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(argv) == 1:
        value = {'q': ""}
    else:
        value = {'q': argv[1]}

    rquest = post(url, data=value)
    try:
        j_son = rquest.json()
        if j_son:
            print("[{}] {}".format(j_son.get("id"), j_son.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
