#!/usr/bin/python3

for num in range(0, 100):
    if num <= 98:
        print(f"{num}".zfill(2) + ", ", end="")
    else:
        print(f"{num} ", end="")
