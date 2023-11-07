#!/usr/bin/python3
import json
from io import StringIO
"""import file"""



def from_json_string(my_str):
    """ocnverts JSON str rep to object

    Args:
        my_str: JSON string
    """

    io = StringIO(my_str)
    obj = json.loads(io)
    return obj
