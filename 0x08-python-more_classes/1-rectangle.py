#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""

class Rectangle:
    """creation of a new instance"""

    def __init__(self, width=0, height=0):
        """creates two instances, width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns the current width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the current width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be a number")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the current height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the current height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be a number")
        elif value < 0:
            raise ValueError("heigt must be  >= 0")
        self.__height = value
