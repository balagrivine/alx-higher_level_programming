#!/usr/bin/python
"""
    function that compares the class type of an object
"""


def is_same_class(obj, a_class):
    """function that checks if an object in an instance of a class
        Args:
            obj: object of a class
            a_class: class

        Return:
            True if object is an instance else False
    """
    return type(obj) is a_class
