#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    i = 0
    new_list = my_list.copy()
    for num in new_list:
        if num % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
        i += 1
    return new_list
