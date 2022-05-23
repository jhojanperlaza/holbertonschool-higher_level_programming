#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        _div = a/b
    except (ValueError, TypeError, ZeroDivisionError):
        _div = None
    finally:
        print("Inside result: {}".format(_div))
    return _div
