#!/usr/bin/python3
# Write a function that prints an integer.
from sys import stderr as stde


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        error = str(e)
        print("Exception: {}".format(error), file=stde)
        return False
