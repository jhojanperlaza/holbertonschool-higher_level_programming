#!/usr/bin/python3

for str in range(122, 96, -1):
    if str % 2 != 0:
        str = str - 32
    print(chr(str), end='')
