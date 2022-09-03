#!/bin/bash
# HTTP HEAD method instead of the GET request with the variable X-HolbertonSchool-User-Id must be sent with the value 98
curl -s "$1" -H "X-HolbertonSchool-User-Id:98"
