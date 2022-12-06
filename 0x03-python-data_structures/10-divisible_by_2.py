#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for n in range(len(my_list)):
        if n % 2 == 0:
            return True
        else:
            return False
