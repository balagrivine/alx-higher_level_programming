#!/usr/bin/python3
"""a rectangle class that returns a formatted string
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
basegeometry for inheritance
"""

class Rectangle(BaseGeometry):
    """Rectangle class

    Args:
        BaseGeometry: parent class
    """

    def __init__(self, width, height):
        """instantiation method

            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calcuates area of the rectangle

        Return:
            area of the rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """returns class instance in str fmt

        Returns:
            output from the string method
        """
        return "[Rectangle] {}/{}" .format(self.__width, self.__height)
