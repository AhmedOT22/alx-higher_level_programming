#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square class"""

    def __init__(self, size = 0, position = (0, 0)):
        """Initializing the class
        Args:
            size: size of the square
            position: posiition in the (x,y) axis
        """

        self.__size = size
        self.__position = position

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
        Raises:
            TypeError: is size is not an integer
            ValuError: if size < 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("message size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position property
            Returns:
                the position
        """
        return self.__position

    @position.setter
    def position(self, value):
    """Size setter
        Args:
            value: tuple of two integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """

        if not isinstance(value, tuple) or len(value) != 2 or \
            not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculate the square area
        Returns: the square of the size
        """

        return self.__size ** 2

    def my_print(self):
        """Returns the position"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
