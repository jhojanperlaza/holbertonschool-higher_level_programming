#!/usr/bin/python3
""" This module contains the class Base """


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
