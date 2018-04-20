#!/usr/bin/python3
def roman_to_int(roman_string):

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    check = 0

    if isinstance(roman_string, str) is False:
        return 0

    r_string = list(roman_string)
    r_string.reverse()
    for char in r_string:
        if r_string.count(char) > 3:
            return 0

    length = len(roman_string)
    for idx in range(length):
        result += roman[roman_string[idx]]
    if len(roman_string) > 1:
        if roman[roman_string[-1]] > roman[roman_string[-2]]:
            result -= roman[roman_string[idx-1]]*2
    return result

# Some Edge cases:

#    if length > 3:
#        for i in range(length-1):
#            if roman[roman_string[i]] < roman[roman_string[i+1]]:
#                check += 1
#    if check >= 1:
#        return 0



#    for elem in r_string:
#        if r_string[0] > elem:
#            check += 1
#        if check > 1:
#            return None
