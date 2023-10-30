#!/usr/bin/python3
"""defines a rectangle class"""

class Rectangle:
    """Reps a rectangle"""

    def __init__(self, width=0, height=0):
        """First instance for the class Rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of the rectangle to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets current height of the rectangle to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("widht must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return (self.__width * self.__height)
    def perimeter(self):
        """retirns the perimeter of the rectangle"""
        return(2 * (self.__width + self.__height))

    def __str__(self):
        """return printable rep of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []

        for row in range(self.__height):
            [rect.append('#') for col in range(self.__width)]

            if row != self.__height - 1:
                rect.appent("\n")
        return ("".join(rect))

    def __repr__(self):
        """returns strign rep of a rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """prints message for every deletion of a rectangle"""
        print("Bye rectangle...")
