#!/usr/bin/python3
"""checks if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """
        Returns True if obj in an instance else False

        Args:
            obj: object
            a_class: class

        Return: True if isinstance else False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
