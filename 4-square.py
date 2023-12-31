#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size  # Use the property setter for validation

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__validate_size(value)
        self.__size = value

    def __validate_size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

