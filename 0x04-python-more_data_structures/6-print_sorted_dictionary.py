#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary)  # sort alphabetize a list
    for i in range(len(sorted_dic)):
        key = sorted_dic[i]
        print(f"{key}: {a_dictionary[key]}")
