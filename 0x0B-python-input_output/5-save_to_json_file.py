#!/usr/bin/python3
import json
"""write function"""


def save_to_json_file(my_obj, filename):
    """function that writes an object to a txt file

    Args:
        my_obj: object
        filename: file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
