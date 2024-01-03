#!/usr/bin/python3
"""This module contains a function that prints a text with 2 new lines after each of these characters: ., ? and :"""

def text_indentation(text):
    """This function prints text with two new lines after each '.', '?', and ':'
    Arguments:
        text (string): the text to be printed.
    Raises:
        TypeError: if text is not a string, with the message: text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    for c in separators:
        text = str(c + '\n\n').join(s.strip() for s in text.split(c))
    print(text, end='')
    if len(text) > 0 and text[-1] in separators:
        print('\n')
