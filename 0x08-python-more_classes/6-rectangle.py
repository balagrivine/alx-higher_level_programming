#!/usr/bin/python3
"""Define a rectangle class"""

class Rectangle:
    """Reps a rectangle
    Attributes:
        number_of_instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new class rectangle

            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """gets the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the current width of the rectangle to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("widthmust be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets value of height to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """claculates area of the rectangle"""
        return (self.__width * self.__height)

    def  perimeter(self):
        """claculates the area of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """reps the rectangle with # chatacters"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []

        for row in self.__height:
            [rect.append('#') for col in range(self.__width)]
            if row != self._height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """rints messag foe deetion of very instance deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
