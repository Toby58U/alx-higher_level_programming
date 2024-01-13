#!/usr/bin/python3
"""Module containing Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class to represent a square deriving from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new square with width and height equal to `size`.

        Args:
            size (int): side lengths of square
            x (int): width offset for drawing square
            y (int): height offset for drawing square
            id: identifier for instance. If None, then object count.

        Raises:
            TypeError: If args are not int (or None for id)
            ValueError: If size is <= 0 or x, y and < 0 or id < 0
        """
        super().__init__(size, size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """Getter/setter for size propetry.
        Uses width attribute from Rectangle parent to store `size`.

        Raises:
            TypeError: If `size` is not an int.
            ValueError: If `size` is <= 0.

        Returns: value associated with `size`.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for `size`."""
        setattr(self, "width", value)
