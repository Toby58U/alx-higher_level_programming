#!/usr/bin/python3

"""Module that defines a base object to be extended by rectangle and square."""

class Base
"""This is the base model that represents the base for all other classes in this project.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
"""

    __nb_object = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
