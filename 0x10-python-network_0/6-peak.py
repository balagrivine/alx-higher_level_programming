#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """A  function to find a peak in a list of unsorted integer"""
    list_of_integers.sort()
    if not list_of_integers:
        return None
    else:
        max_int = max(list_of_integers)
    return max_int
