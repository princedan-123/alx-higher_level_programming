#!/usr/bin/python3
# a function that deletes a key in a dictionary.
def simple_delete(a_dictionary, key=""):
    count = len(a_dictionary)
    for i in range(0, count):
        if i == key:
            a_dictionary.pop(i)
    return a_dictionary
