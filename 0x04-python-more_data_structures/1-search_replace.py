#!/usr/bin/python3
# function that replaces all occurrences of an element by another in a new list.
def search_replace(my_list, search, replace):
    if my_list:
        check = lambda x: replace if x == search else x
        new_list = list(map(check, my_list))
    return new_list
