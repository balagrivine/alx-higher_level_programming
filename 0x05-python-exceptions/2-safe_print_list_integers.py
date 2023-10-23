#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for i in range(0, x):
        try:
            fmt = "{:d}".format(my_list[i]))
            print(fmt, end=' ')
            ret += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (ret)
