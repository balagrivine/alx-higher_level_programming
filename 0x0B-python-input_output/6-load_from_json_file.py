#!/usr/bin/python3
"""importing json and stringIO
"""

import json
from io import StringIO
"""reading from json file
"""


def load_from_json_file(filename):
    """creates object from json file

    Args:
        filename: name of the file
    Returns:
        object
    """

    with open(filename, "r", encoding="utf-8") as f:
        read = f.read()
        io = StringIO(read)
        return json.load(io)
