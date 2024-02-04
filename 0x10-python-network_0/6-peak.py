#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """A  function to find a peak in a list of unsorted integer"""
    list_of_integers.sort()
    """if not list_of_integers:
        return None
    else:
        max_int = max(list_of_integers)"""
    max_int = 0
    for num in range(list_of_integers):
        if list_of_integers[num + 1] >= list_of_integers[num]:
            max_int = list_of_integers[num + 1]
    return max_int
