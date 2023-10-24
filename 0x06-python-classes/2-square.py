#!/usr/bin/python3
"""Defines a class"""


class Square():
    """Initialize a class"""
    def __init__(self, size=0):

        """
            Initialize a new square

        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
