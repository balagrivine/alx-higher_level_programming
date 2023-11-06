#!/usr/bin/python3
"""
    function to check instance of objects
"""


def is_kind_of_class(obj, a_class):
    """
        Returns True if obj is an instance of a_class

        Args:
            obj: object
            a_class: class
        Return:
            True if successful else False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
