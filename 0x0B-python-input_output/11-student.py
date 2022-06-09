#!/usr/bin/python3
"""

class Student

"""


class Student:

    def __init__(self, first_name, last_name, age):
        """ initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return a diccionary with the
        instances of a students
        """
        if attrs is None:
            return vars(self)
        new_dict = {}
        for key, value in vars(self).items():
            for keys in attrs:
                if key == keys:
                    new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        """
        En esta caso self nos sirve como
        parametro de objeto para
        setattr
        """
        for key, value in json.items():
            setattr(self, key, value)
