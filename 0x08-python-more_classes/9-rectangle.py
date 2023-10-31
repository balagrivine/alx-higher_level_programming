#!/usr/bin/python3
"""Defines a rectangle class"""

class Rectangle:
    """reps a rectangls
        Attributes:
            number_of_instances: number of Rectangle instances
            print_symbol: The symbol used to print the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width: width of the new rectangle
            height: height of the new rectangle
        """
        self.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets current heifht of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """stes current height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("haight must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns area of the bigger rectangle

        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """"returns new rectangle with width and height equal to size"""
        return (cls(size, size))

    def __str__(self):
        """returns printable rep of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return("")

        rect = []
        for row in range(self.__height):
            [rect.append(str(self.print_symbol)) for col in range(self.__width)]
            if row != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """returns string representation of a rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """prints a message forevery deletion of a rectangle"""
        self.number_of_instances -= 1
        print("Bye rectanngle...")
