#!/usr/bin/python3
def no_c(my_string):
    add = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        add += i
    return add
