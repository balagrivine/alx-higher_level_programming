#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest = 0
    best = None

    for k, v in a_dictionary.items():
        if v > highest:
            highest = v
            best = k
    return best
