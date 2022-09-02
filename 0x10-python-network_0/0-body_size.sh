#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
# and displays the size of the body of the response
# -i: Include the HTTP response headers in the output
# -s: Avoid showing progress bar

curl -si $1 | awk '/Content-Length/ {print $2}'
