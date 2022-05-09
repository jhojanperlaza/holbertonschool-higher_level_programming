def new_in_list(my_list, idx, element):
    a = my_list.copy()
    if idx < 0:
        return a
    if idx > len(my_list):
        return a
    a[idx] = element
    return a
