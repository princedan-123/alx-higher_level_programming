#!/usr/bin/python3
def print_last_digit(number):
    if number in range(0, 10):
        return number
    elif number in range(-1, -10,1):
        return number
    else:
        number = number % 10
        return number
