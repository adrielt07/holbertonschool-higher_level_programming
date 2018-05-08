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

    new_text = "".join(n if n not in special_ch else n + "\n\n" for n in text)

    print("\n".join(n.strip() for n in new_text.split("\n")), end="")
