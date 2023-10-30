#!/usr/bin/python3
"""defines a class Rectangle"""

class Rectangle:
    """create instances for the class"""

    def __init__(self, width=0, height=0):
        """first instance of the class Rectange
            Args:
                width: width of the erctangle
                height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the current width of the ectangle to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the current height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectaangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        return (2 * (self.__width + self.__height))
