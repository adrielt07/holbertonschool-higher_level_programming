#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r") as f:
        buffer = list(f)

    with open(filename, "w") as o:
        for elem in buffer:
            if search_string in elem:
                elem = elem + new_string
            o.write(elem)
