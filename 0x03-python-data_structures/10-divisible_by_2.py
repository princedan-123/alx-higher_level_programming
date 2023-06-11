#!/usr/bin/python3
# Write a function that finds all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    count = len(my_list)
    replica = []
    for i in range(0, count):
        if my_list[i] % 2 == 0:
            replica.append(True)
            return replica
        elif my_list[i] % 2 != 0:
            replica.appenad(False)
            return replica
