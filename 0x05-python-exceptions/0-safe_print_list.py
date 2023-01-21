#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numAdd = 0
    for p in range(x):
        try:
            print("{}".format(my_list[p]), end='')
            numAdd += 1
        except IndexError:
            break
    print()
    return (numAdd)
