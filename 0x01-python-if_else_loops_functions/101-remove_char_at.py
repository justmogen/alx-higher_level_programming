#!/usr/bin/python3
def remove_char_at(str, n):
    # function that creates a copy of the string, removing the character at the
    # position n (not the Python way, the “C array index”).
    if n < 0:
        return (str)  # if no index specified -> original string
    return (str[:n] + str[n+1:])
    # print upto specified index but not including it
    # jump over specified index by 1 and print to end
