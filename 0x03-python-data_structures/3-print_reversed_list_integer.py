#!/usr/bin/python3
# Write a function that prints all integers of a list, in reverse order.
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    count = len(my_list)
    for i in range(count):
        print("{}".format(new_list[i]))
