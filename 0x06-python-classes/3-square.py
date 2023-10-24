#!/usr/bin/python3
"""Define a class square"""


class Square():
    """initialize a new area"""

    def __init__(self, size):
        """Initialize new square

        Args:
            size: size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
