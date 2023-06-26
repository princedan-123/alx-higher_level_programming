#!/usr/bin/python3
# Write a function that divides 2 integers and prints the result.
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    except Exception:
        return None
    finally: 
        print("inside result: {}".format(result))
