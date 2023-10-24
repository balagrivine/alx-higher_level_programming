#!/usr/bin/python3
"""Define a class Square"""

class Square():
    """Initialize a new square"""

    def __init__(self, size=0):
        """Initialize a  square
        Args:
            size: size of the square
        """
        self.__size = size

    @property
    def size(self):
        """gets the current size of the square"""
        return (self.__size)
    @size.setter
    def size(self, value):
        """lets size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """retrns current area of the square"""
        return (self.__size * self.__size)
