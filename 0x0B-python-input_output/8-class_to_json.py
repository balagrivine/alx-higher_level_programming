#!/usr/bin/python3
"""serializing objects and
simple data types
"""


def class_to_json(obj):

    """unction that returns the dictionary description
            with simple data structure (list, dictionary, string,
            integer and boolean) for JSON serialization of an object

        Args:
            obj (obj): instance of a class
        Returns:
            dict:  dictionary description with simple data structure
    """


if type(obj) in (str, int, bool):
    return obj
elif isinstance(obj, list):
    return [class_to_json(item) for item in obj]
elif isinstance(obj, dict):
    return {key: class_to_json(value) for key, value in obj.items()}
else:
    attributes = {}
    for attr_name, attr_value in obj, __dict__.items():
        attributes[attr_name] = class_to_json(attr_value)
    return attribues
