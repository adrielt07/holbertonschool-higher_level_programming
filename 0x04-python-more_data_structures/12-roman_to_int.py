#!/usr/bin/python3
def roman_to_int(roman_string):

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    check = 0

    if isinstance(roman_string, str) is False:
        return 0

    length = len(roman_string)
    for idx in range(length):
        result += roman[roman_string[idx]]
    for indx in range(length):
        if indx > 0:
            if roman[roman_string[indx-1]] < roman[roman_string[indx]]:
                result -= roman[roman_string[indx-1]]*2
    return result
