#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    element = 0
    for element in my_list[:x]:
        try:
            print(element, end="")
        except ValueError:
            break
    print()
    return element
