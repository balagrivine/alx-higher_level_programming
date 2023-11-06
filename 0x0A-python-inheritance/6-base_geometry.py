#!/usr/bin/python3


"""A class based on 5-geometry"""
class BaseGeometry:
    """Create first instance of the class"""
    def __init__(self):
        """Takes no arguments and does nothing"""
        pass

    def area(self):
        raise Exception("area() is not implemented")
