#!/usr/bin/python3
def uppercase(str):
    add = ""
    for l in str:
        ch = ord(l)
        if ch in range(97, 123):
            ch = ch - 32
            add = add + chr(ch)
        else:
            add = add + chr(ch)
    print("{}".format(add))
