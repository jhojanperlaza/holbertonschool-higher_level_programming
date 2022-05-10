#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_list1 = set(set_1)
    set_list2 = set(set_2)
    return set_list1 | set_list2  # the operator | is the clave
