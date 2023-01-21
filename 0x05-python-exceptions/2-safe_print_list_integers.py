#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numAdd = 0
    for p in range(x):
        try:
            print("{:d}".format(my_list[p]), end='')
            numAdd += 1
        except (TypeError, ValueError):
            continue
    print()
    return (numAdd)
