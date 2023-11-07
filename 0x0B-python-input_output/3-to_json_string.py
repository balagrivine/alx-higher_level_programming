#!/usr/bin/python3
"""write function"""
import json


def to_json_string(my_obj):
    """function that returns JSON rep of a string

    Args:
        my_obj: python object
    """

    rep = json.dumps(my_obj)
    return rep
