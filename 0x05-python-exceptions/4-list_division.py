#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = [0 for _ in range(list_length)]
    index = 0
    for num1, num2 in zip(my_list_1, my_list_2):
        try:
            _div = (num1 / num2)
        except(TypeError):
            print("wrong type")
            _div = 0
        except(ZeroDivisionError):
            print("division by 0")
            _div = 0
        finally:
            new_list[index] = _div
        index += 1
    if index != list_length:
        print("out of range")
    return new_list
