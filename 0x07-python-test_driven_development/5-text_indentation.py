#!/usr/bin/python3
"""

    this module prints 
    a text with 2 new lines after each of these 
    characters: ., ? and :

"""

def text_indentation(text):
    """
    Args:
        text: is the text to delimit
    Returns:
        each line of text delimited
    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip( )
    is_new_line = True
    for chars in text:
        if chars == '.':
            print(chars)
            print('\n', end = '')
            is_new_line = True
            continue
        if chars == '?':
            print(chars)
            print('\n', end = '')
            is_new_line = True
            continue
        if chars == ':':
            print(chars)
            print('\n', end = '')
            is_new_line = True
            continue
        if is_new_line == True:
            if chars == ' ':
                continue
            is_new_line = False
        print(chars, end='')
