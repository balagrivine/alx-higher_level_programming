#!/usr/bin/python3
"""Defines a rectangle class"""

class Rectangle:
    """Represents a rectangle

        Attributes: number_of_instances: number of rectangle instances
        print_symbol: symbol used for string representation

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width: width of the rectangle
            height: height f the ectangle
        """
        self.__width = width
        self.__height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """gets current eidth of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets current width of the rectangle to value"""
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
        """sest current height of the ectangle to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returs the perimeter of the rectangle"""
        if self.__width == 0 or self.__heigh == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """returns strign rep f the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for row in range(self.__height):
            [rect.append(str(self.print_symbol)) for col in range(self.__width)]
            if row != self.__height -1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """ reps string"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """deletes each and every instance of a string occuerence"""
        self.number_of_instances -= 1
        print("Bye rectangle...")
