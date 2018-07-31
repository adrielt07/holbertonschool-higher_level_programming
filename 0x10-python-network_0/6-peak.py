#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    finds a peak in the list of integers
    """
    if len(list_of_integers) == 0 or list_of_integers is None:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = len(list_of_integers) / 2
    mid = int(mid)
    try:
        if list_of_integers[mid - 1] < list_of_integers[mid]\
           and list_of_integers[mid + 1] < list_of_integers[mid]:
            return list_of_integers[mid]
    except IndexError:
        if list_of_integers[mid - 1] < list_of_integers[mid]:
            return list_of_integers[mid]
    if list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
