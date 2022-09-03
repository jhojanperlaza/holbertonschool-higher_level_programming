#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -I -sX OPTIONS "$1" | awk '/Allow/'| cut -d " " -f2-
