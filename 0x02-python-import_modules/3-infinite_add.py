#!/usr/bin/python3
import sys

if __name__ == '__main__':

    i = 1
    result = 0
    number_arg = (len(sys.argv))-1
    while i <= number_arg:
        result = result + int(sys.argv[i])
        i += 1
    print(result)
