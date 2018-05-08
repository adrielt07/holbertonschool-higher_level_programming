#!/usr/bin/python3
"""
Module 5-text_indentation:
def(s):
1) text_indentation - prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    text_indentation - prints a text with 2 new lines after
    each of these characters: ., ? and :
    No space at the beginning or at the end of every new line
    Requirement:
    1) text must be a string
    """
    special_ch = [':', '?', '.']
    i = 0
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    l = text.split()

    for n in range(len(l)):
        if l[n][-1] in special_ch:
            print(l[n] + "\n")
        else:
            if n == len(l) - 1:
                print(l[n], end="")
            else:
                print(l[n], end=" ")


#text_indentation("Holberton. School? How are you:    John")
