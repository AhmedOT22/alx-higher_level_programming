#!/usr/bin/python3
"""defines a square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """Initialize the square class
        Args:
            size - the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: is size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self._size = size
