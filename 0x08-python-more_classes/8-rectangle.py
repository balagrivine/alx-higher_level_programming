#!/usr/bin/python3
"""Define a rectangle"""

class Rectangle:
    """create first instance of the class
        Attributes:
            number_of_instances: number of instances of the erctangle
            print_symbol: prints using `#`
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instance of the class rectangle

            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.__height = height
        self.__width = width
        self.number_of_instances += 1

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width + self.__width

    @width.setter
    def width(self, value):
        """sets current width of the rectangle to value"""
        if not isinstance(value, int):
            raise TypeError("width must eb an integer")
        elif value < 0:
            raise ValueError("widht must be >= 0")

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
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """returns the current area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns rectangle with the greatest area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an isnstance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """returns string rep of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        rect = []
        for row in range(self.__height):
            [rect.append(str(self.print_string)) for col in range(self.__width)]
            if row != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """returns strign rep of a rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"

    def __del__(self):
        """prints for every deletion of  arectangle"""
        self.number_of_instances -= 1
        print("Bye rectangle...")
