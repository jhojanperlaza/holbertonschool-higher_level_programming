#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':

    string_name = dir(hidden_4)
    for string in string_name:
        if string[0:2] != '__':
            print (string)





