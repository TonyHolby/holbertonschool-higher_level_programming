#!/usr/bin/python3
"""
    Prints a text with 2 new lines after each of these characters: ., ? and :
    
    Parameter:
        text (str): A string.

    Raise:
        TypeError: If text is not a string.
"""


def text_indentation(text):
    """ Prints a new text with indentation. """
    if not isinstance(text, str):
        raise TypeError("text must be a string")   
    new_text = ""
    character = 0
    while character < len(text):
        if text[character] in ".?:":
            new_text += text[character] + "\n\n"
            character += 1
            while character < len(text) and text[character] == ' ':
                character += 1
        else:
            new_text += text[character]
            character += 1
    print(new_text, end="")
