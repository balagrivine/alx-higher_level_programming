#!/usr/bin/python3

"""class Rectangle"""
class Rectangle:
    """first instance of class Rectangle"""
    def __init__(self, width=0, height=0):
        """instance of the classRectangle
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
        """sets current width of the rectange to value"""
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
        """sets the cerrent value of the rectangle to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """prints the rectangle with the character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for row in range(self.__height):
            [rect.append('#') for column in range(self.__width)]
            if row != self.height - 1:
                rect.append('\n')
        return ("".join(rect))

    def __repr__(self):
        """returns string representation of a rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
