#!/usr/bin/python3
def roman_to_int(roman_string):

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_string = list(roman_string)
    r_string.reverse()
    result = 0
    check = 0

    for char in r_string:
        if r_string.count(char) > 3:
            return None

    length = len(roman_string)
    if length > 3:
        for i in range(length-1):
            if roman[roman_string[i]] < roman[roman_string[i+1]]:
                check += 1
    if check >= 1:
        return None
    for idx in range(length):
        result += roman[roman_string[idx]]
    if len(roman_string) > 1:
        if roman_string[length-1] > roman_string[length-2]:
            result -= roman[roman_string[idx-1]]*2
    return result
#    for elem in r_string:
#        if r_string[0] > elem:
#            check += 1
#        if check > 1:
#            return None
