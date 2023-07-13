#!/usr/bin/python3
"""A script that creates a class"""


class Base:
    """A class called Base that will manage id attribute in future classes
    atrributes
        __nb_objects
        constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """A constructor that initialises an object
            arguments
                id:(int) an integer value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
