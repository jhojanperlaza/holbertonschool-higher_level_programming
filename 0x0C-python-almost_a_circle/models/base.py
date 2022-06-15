#!/usr/bin/python3
""" This module contains the class Base """
import json

class Base:
    """ This is class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor that initialize instance attributes"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            """ other form is 'Base.__nb_objects += 1' """
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
            if list_dictionaries is None or list_dictionaries == " ":
                return "[]"
            return json.dumps(list_dictionaries)
