#!/usr/bin/python3
"""A function to rturn list of variables"""


def lookup(obj):
    """Function that returns a list of available attributes and methods"""
    return dir(obj)
