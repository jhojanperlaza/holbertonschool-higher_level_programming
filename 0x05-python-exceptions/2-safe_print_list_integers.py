#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for element in my_list[:x]:
        try:
            print("{:d}".format(element), end="")
            cont += 1
        except (ValueError, TypeError):
            pass
    print()
    return cont
