#!/usr/bin/python3
"""defines a square"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square class
        Args:
            size: the size of the square
            position: coordinate of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: is size is less than 0
        """

        self.size = size
        self.position

    def __str__(self):
        self.my_print()

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

    @property
    def position(self):
        """retrieves the position
        Raises:
            TypeError: if value != a tuple of 2 int < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square
        Args: value as a tuple of 2 int
        Raises:
            TypeError: if value != a tuple of 2 int < 0
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculate the area of the square
        Returns: the square of the size
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the position"""
        pos = ""
        if self.size == 0:
            return "\n"
        for i in range(self.position[1]):
            pos += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                pos += " "
            for k in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """prints the square in position"""
        print(self.pos_print(), end="")
