#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_value = 0
    if not roman_string or roman_string is None:
        return 0
    for letter in range(len(roman_string)):
        if letter < len(roman_string) - 1:
            if roman_d[roman_string[letter]] < roman_d[roman_string[letter+1]]:
                roman_value -= roman_d[roman_string[letter]]
            else:
                roman_value += roman_d[roman_string[letter]]
        else:
            roman_value += roman_d[roman_string[letter]]
    return roman_value