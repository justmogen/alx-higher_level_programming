#!/usr/bin/python3
for ix in range(0, 10):
    for ixx in range(ix + 1, 10):
        if ix == 8 and ixx == 9:
            print("{}{}".format(ix, ixx))
        else:
            print("{}{}".format(ix, ixx), end=', ')
