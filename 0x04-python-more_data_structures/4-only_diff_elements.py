#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    my_set = set()
    for x in set_1:
        for y in set_2:
            if x not in set_2 or y not in set_1:
                my_set.add(x)
                my_set.add(y)
    return my_set
