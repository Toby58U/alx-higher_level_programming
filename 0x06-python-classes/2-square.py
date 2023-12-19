#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.__size = size
        self.__validate_size()
    def __validate_size(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
