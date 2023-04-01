#!/usr/bin/python3
"""Peak fining algorithm"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsprted integers.
    Args:
        list_of_integers (list): A list of unsorted integers

    Return:
        int: the peak value
    Complexity:
        0(log(n)) Binary search approach in best case and 0(n) in worst case.

    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peakV = list_of_integers[mid]

    if peakV > list_of_integers[mid - 1] and peakV > list_of_integers[mid + 1]:
        return peakV
    elif peakV < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
