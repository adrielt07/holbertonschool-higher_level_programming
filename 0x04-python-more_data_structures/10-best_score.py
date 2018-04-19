#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    a = (sorted(a_dictionary.values()))
    if len(a) == 0:
        return None

    val = (a[len(a)-1])
    for k, v in a_dictionary.items():
        if v == val:
            return k
