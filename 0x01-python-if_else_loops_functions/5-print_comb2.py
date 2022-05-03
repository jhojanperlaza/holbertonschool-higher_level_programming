#!/usr/bin/python3

for num in range(0, 100):
    if num <= 98:
        print(f"{num:02d}, ".format(num), end='')
    else:
        print(f"{num:02d}".format(num))
