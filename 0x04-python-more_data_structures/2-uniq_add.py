#!/usr/bin/python3

def uniq_add(my_list=[]):
    add = 0
    my_set = set()
    for x in my_list:
        if x not in my_set:
            my_set.add(x)
            add += x
    return add
