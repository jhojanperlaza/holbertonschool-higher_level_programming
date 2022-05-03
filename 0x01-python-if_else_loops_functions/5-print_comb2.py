#!/usr/bin/python3

for num in range(0, 100):
    if num <= 98:
        print("{}".format(num).zfill(2) + ", ", end="")
    else:
        print("{}".format(num), end="")
