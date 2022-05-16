#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string:
        return 0
    if not isinstance(roman_string, str):  # if no is a string
        return 0
    dic_roman = {'X': 10, 'I': 1, 'V': 5,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def comparator(letter):
        result, i = 0, 0
        for key in dic_roman:
            if key == letter:
                result = result + dic_roman[letter]
                return result

            if letter == 'I':
                index = roman_string.index('I')
                if index < len(roman_string)-1:
                    if roman_string[index+1] != 'I':
                        return -1
        return result

    comp = list(map(comparator, roman_string))
    return sum(comp)
