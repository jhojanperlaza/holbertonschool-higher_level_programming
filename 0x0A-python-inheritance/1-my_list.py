#!/usr/bin/python3

class list:

    def __init__(self):
        self.list = []

    def append(self, num):
        if type(num) is not int:
            raise TypeError("Must be an integer")
        self.list += [num]
        return self.list

    def print_sorted(self):
        print(sorted(self.list))

    def __str__(self):
        return str(self.list)


class MyList(list):
    pass
