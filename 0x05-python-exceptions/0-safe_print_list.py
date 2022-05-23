#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for num in my_list[:x]:
            print(int(num), end="")
        print()
    except ValueError:
        return
    return num
