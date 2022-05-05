#!/usr/bin/python3
import sys

if __name__ == '__main__':

    i = 1
    number_arg = (len(sys.argv))-1
    if number_arg == 0:
        print("0 arguments.")
    elif number_arg == 1:
        print("1 argument:")
        print("1: " + sys.argv[1])
    elif number_arg > 1:
        print(f"{number_arg} arguments:")
        while i <= number_arg:
            print(f"{i}: " + sys.argv[i])
            i += 1
