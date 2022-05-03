#!/usr/bin/python3

for num in range(0, 10):
    for num2 in range(1, 10):
        if num != num2 and num < num2:
            print (f"{num}{num2}", end="")
            if (num != 8):
                print (", ", end="")
print ()