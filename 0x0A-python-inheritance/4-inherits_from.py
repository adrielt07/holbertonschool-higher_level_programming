#!/usr/bin/python3
def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class) is True:
        return True
    else:
        return False
