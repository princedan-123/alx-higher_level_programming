#!/usr/bin/python3
# Write a function that adds 2 tuples.
def add_tuple(tuple_a=(), tuple_b=()):
    count1 = len(tuple_a)
    count2 = len(tuple_b)
    first = list(tuple_a)
    second = list(tuple_b)
    if count1 == 0:
        first[0, 0]
    elif count1 == 1:
        first.append(0)
    if count2 == 0:
        second = [0, 0]
    elif count2 == 1:
        second.append(0)
    a = first[0] + second[0]
    b = first[1] + second[1]
    result = (a, b)
    return result
