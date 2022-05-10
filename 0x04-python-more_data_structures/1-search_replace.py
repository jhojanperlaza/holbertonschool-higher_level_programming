#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def change(num):
        if num == search:
            num = replace
            return num
        return num
    new_list = my_list.copy()
    new_list = list(map(change, new_list))
    print(new_list)
