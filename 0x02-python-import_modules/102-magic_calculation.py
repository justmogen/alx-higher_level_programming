#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        h = add(a, b)
        for n in range(8, 10):
            h = add(h, n)

        return (h)
    else:
        return(sub(a, b))
