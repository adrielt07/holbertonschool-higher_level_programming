#!/usr/bin/python3
def roman_to_int(roman_string):

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_string = list(roman_string)
    result = 0
    for char in r_string:
        if r_string.count(char) > 3:
            return None

    length = len(roman_string)
    for idx in range(length):
        result += roman[roman_string[idx]]
    if len(roman_string) > 1:
        if roman_string[length-1] > roman_string[length-2]:
            result -= roman[roman_string[idx-1]]*2
    return result
