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

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    for idx in range(len(text)):
        if text[idx] == " " and text[idx - 1] in special_ch:
            print("", end="")
        else:
            print(text[idx], end="")

        if text[idx] in special_ch:
            print("\n")
