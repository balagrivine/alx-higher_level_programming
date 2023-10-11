#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary

    new_dict.update((k, v * 2) for k, v in new_dict.items())
    return new_dict
