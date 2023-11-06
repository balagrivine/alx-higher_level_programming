#!/usr/bin/python3


"""create a class based on 6-base_geometry"""
class BaseGeometry:
    """create first instance of the class"""
    def __init__(self):
        """takes no argument"""
        pass

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer" .format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))
