#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    count = len(my_list)
    for i in range(count):
        print("{}".format(new_list[i]))
