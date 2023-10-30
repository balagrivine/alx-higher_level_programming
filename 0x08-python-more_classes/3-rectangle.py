#!/usr/bin/python3

"""define a class Rectangle"""
class Rectangle:
    """create an instance of the class rectangle"""

    def __init__(self, width=0, height=0):
        """firts instance of the class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """erturns the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the current width of the rectangle to value"""
        if not isinstance(value, int):
            raise TypeError("widht must be an integer")
        elif value < 0:
            raise ValueError("Width must be  > 0")
        self.__width = value

    @property
    def height(self):
        """returns the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """claculates and retiurns the area of a rectangle"""
        return self.__width * self.__height
        for _ in range(self.__height):
            for _ in range(self.__width):
                print("#", end="")
            print()

    def perimeter(self):
        """calculates and returns the perimeter of a rectangle"""
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """returnd printabe representation odf a string"""
        if self.__width == 0 or self.__height == 0:
            return("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return ("".join(rect))
