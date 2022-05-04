#!/usr/bin/python3

def print_last_digit(number):

    last = number
    if number < 0:
        last = ((last) * -1) % 10
        print (last, end="")
        return (last)
    else:
        last = last % 10
        print (last, end="")
        return (last)
