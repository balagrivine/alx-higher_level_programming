#!/usr/bin/pyton3
import json
"""import file"""


def from_json_string(my_str):
    """ocnverts JSON str rep to object

    Args:
        my_str: JSON string
    """

    obj = json.loads(my_str)
    return obj
