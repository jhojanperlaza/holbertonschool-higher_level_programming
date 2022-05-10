#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_list1 = set(set_1)
    com_elements = set_list1.intersection(set_2)  # intersection is the clave
    format_result = list(com_elements)
    return format_result
