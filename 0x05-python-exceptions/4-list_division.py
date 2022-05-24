#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        try:
            _div = (my_list_1[index] / my_list_2[index])
        except(TypeError):
            print("wrong type")
            _div = 0
        except(ZeroDivisionError):
            print("division by 0")
            _div = 0
        except(IndexError):
            print("out of range")
            _div = 0
        finally:
            new_list.insert(index, _div)
    return new_list
