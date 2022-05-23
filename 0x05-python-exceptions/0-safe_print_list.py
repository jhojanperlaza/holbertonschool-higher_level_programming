#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for element in my_list[:x]:
        try:
            print(int(element), end="")
        except ValueError:
            print(element, end="")
    print()
    return element
