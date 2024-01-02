#!/usr/bin/python3
"""This function adds two integers."""

def add_integer(a, b=98):
    """This definition returns an integer: the addition of a and b
    a and b must be first casted to integers if they are float
    a and b must be integers or floats, otherwise raise a TypeError exception with the message 
        a must be an integer 
        OR
        b must be an integer.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a+b)
