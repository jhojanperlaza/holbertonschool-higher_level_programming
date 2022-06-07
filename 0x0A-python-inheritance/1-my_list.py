#!/usr/bin/python3

"""

this program is the first methods inheritance
of class for my

"""


class MyList(list):
    """
    this class performs all the methods
    of the class MyList
    """

    def print_sorted(self):
        """
        this method this method organizes the
        list from smallest to largest
        """
        print(sorted(self))
