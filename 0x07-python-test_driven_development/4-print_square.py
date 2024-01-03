#!/usr/bin/python3
"""This module contains a function that prints a square with the character #."""

def print_square(size):
    """This is a function that prints a square with the character #.
    Arguments:
        size: An integer representing the height or width of the square.
    Raises:
        TypeError: If size is not an integer, with the message: size must be an integer.
        ValueError: If size is < 0, with the message: size must be >= 0
        TypeError: if size is a float and is less than 0, with the message: size must be an integer.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size.is_integer():
            size = int(size)
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
