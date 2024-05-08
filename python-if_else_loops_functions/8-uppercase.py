#!/usr/bin/python3
def uppercase(string):
    for character in string:
        if ord(character) >= 97 and ord(character) <= 122:
            character = chr(ord(character) - 32)
        print("{}".format(character), end="")
    print("")
    