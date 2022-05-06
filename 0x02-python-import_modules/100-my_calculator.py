#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == '__main__':

    result = ""
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    s = sys.argv[2]
    if s != '+' and s != '-' and s != '*' and s != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        result = add(a, b)
    if sys.argv[2] == '-':
        result = sub(a, b)
    if sys.argv[2] == '*':
        result = mul(a, b)
    if sys.argv[2] == '/':
        result = div(a, b)
    print(f"{a} {s} {b} = {result}")
