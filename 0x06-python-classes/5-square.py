#!/usr/bin/python3
"""Defien a class square"""


class Square():
    """Initialize square"""
    def __init__(self, size):
        """Initialize new square
        Args:
            size: sizze of the new square
        """
        self.__size = size

    @property
    def size(self):
        """gets the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with a character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
