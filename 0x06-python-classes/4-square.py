#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square class"""

    def __init__(self, size = 0):
        """Initializing the class
        Args:
            size: size of the square
        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """Size property
            Returns:
                the square of size
        """
        return self.__size

    @size.setter
    def size(self, value):
    """Size setter
        Args:
            value: the size of the square
        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the square area
        Returns: the square of the size
        """

        return self.__size ** 2
