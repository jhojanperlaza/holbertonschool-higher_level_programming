#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    index = 0
    for num1, num2 in zip(my_list_1[:list_length], my_list_2[:list_length]):
        try:
            _div = (num1 / num2)
        except(ValueError, TypeError, ZeroDivisionError):
            _div = 0
        finally:
            new_list.insert(index, _div)
        index += 1
    return new_list
