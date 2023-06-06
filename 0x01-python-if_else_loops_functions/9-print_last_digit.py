#!/bin/python3
def print_last_digit(number):
    if number >= 0 and number <=9:
        return number
    else:
        return number % 10
