#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    my_list[idx] = element
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    return (None if idx < 0 and idx > len(my_list) else my_list)
