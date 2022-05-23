#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    element = 0
    for element in my_list[:x]:
        try:
            int(element)
            print("{:d}".format(element),end="")
        except (ValueError, TypeError):
            continue
    print()
    return element
