#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square class"""

    def __init__(self, size = 0):
        """Initializing the class
        Args:
            size - size of the square
        Raises:
            TypeError: if size is not an integer
            ValuError: if size < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        Calculate the square area
        Returns: the square of the size
        """

        return self.__size ** 2
