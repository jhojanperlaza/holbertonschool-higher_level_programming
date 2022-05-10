#!/usr/bin/python3
def uniq_add(my_list=[]):

    result = 0
    int_repeated = set(my_list)  # remove int repeated
    unique_list = (list(int_repeated))  # convert in list
    for num in unique_list:
        result = result + num
    return result
