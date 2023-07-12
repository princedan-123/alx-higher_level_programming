#!/usr/bin/python3
"""A script that appends a string to a file"""


def append_after(filename="", search_string="", new_string=""):
    """A function that appends a string to a file after the occurence
        of a particular string
        parameters:
            filename: the name of the file
            search_string: the string after which appending occurs
            new_string: the new string to be appended
    """
    lenght = len(search_string)
    with open(filename, "a+") as f:
        while f:
            content = f.readline()
            if content == "":
                break
            for i in content:
                if i == search_string:
                    f.write(new_string)
