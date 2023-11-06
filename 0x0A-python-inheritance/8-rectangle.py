#!/usr/bin/python3

"""a rectangle class with instantiation
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    getting the BaseGeometry class for inheritace
"""

class Rectangle(BaseGeometry):
    """create first instance of the class"""
    def __init__(self, width, height):
        """Python instantiation method
            Args:
                height: height of the rectangle
                width: width of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
