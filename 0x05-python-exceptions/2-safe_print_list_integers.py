#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            cont += 1
        except (ValueError, TypeError):
            pass
    print()
    return cont
