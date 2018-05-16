#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename) as f:
        for num, line in enumerate(f):
            if num > 0:
                if num == nb_lines:
                    break
            print(line, end="")
