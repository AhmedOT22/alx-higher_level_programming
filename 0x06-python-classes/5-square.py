#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square class"""

    def __init__(self, size = 0):
        """Initialize an instance
        Args:
            size: size of the square
        """

        self.__size = size

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

    def area(self):
         """
        Calculate the square area
        Returns: the square of the size
        """

        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
