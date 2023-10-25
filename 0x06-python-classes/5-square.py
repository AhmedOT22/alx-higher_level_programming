#!/usr/bin/python3
"""defines a square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """Initialize the square class
        Args:
            size: the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: is size is less than 0
        """

        self.__size = size

    @property
    def size(self):
        """retrives the size"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        calculate the area of the square
        Returns: the square of the size
        """

        return (self.__size ** 2)

    def my_print(self):
        """prints the square in #"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
