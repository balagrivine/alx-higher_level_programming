#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    my_list[idx] = element

    return (None if idx < 0 and idx > len(my_list) else my_list)
