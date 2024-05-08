#!/usr/bin/python3
def majuscule(string):
    for character in string:
        if 'a' <= character <= 'z':
            uppercase_char = chr(ord(character) - 32)
        else:
            character
        print('{}'.format(uppercase_char), end='')
    print()
    