#!/usr/bin/python3
"""

this program is the first methods inheritance
of class for my

"""


class list:
    """
    this class performs all the methods
    of the class MyList
    """

    def __init__(self):
        """ contructor of class list """
        self.list = []

    def append(self, num):
        """ this method adds items to the list """
        if type(num) is not int:
            raise TypeError("Must be an integer")
        self.list += [num]
        return self.list

    def print_sorted(self):
        """
        this method this method organizes the
        list from smallest to largest
        """
        print(sorted(self.list))

    def __str__(self):
        """prints the list when call print(Mylist)"""
        return str(self.list)


class MyList(list):
    pass
