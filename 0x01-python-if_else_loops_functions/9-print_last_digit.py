#!/usr/bin/python3
def print_last_digit(number):
    if number in range(0, 10):
        print(number, end="")
        return number
    elif number in range(-1, -10, 1):
        print(number, end="")
        return number
    else:
        number = number % 10
        print(number, end="")
        return number
