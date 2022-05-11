#!/usr/bin/python3

def roman_to_int(roman_string):
    dic_roman = {'X':10,'I':1,'V':5, 'L':50,'C':100,'D':500,'M':1000}
    def comparator(letter):
        result, i = 0, 0
        for char in roman_string:
            if char == letter:
                result = result + dic_roman[letter]
            i = i+1
        return result

    comp = list(map(comparator, dic_roman))
    return sum(comp)
