#!/usr/bin/python3
"""finds peak in list of ints"""


def find_peak(list_of_integers):
    """Finds a peak in the list."""
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2

        if (mid == 0 or list_of_integers[mid - 1]
            <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1]
                <= list_of_integers[mid]):
            return list_of_integers[mid]

        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1
