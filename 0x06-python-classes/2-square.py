#!/usr/bin/python3

"""Define a class Square."""
class Square:
    """Represent a square."""
    def __init__(self, size=0):
        self.__size = size
        self.__validate_size()
    def __validate_size(self):

        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
