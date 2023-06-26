#!/usr/bin/python3
# Write a function that divides 2 integers and prints the result.
def safe_print_division(a, b):
    try:
        answer = None
        answer = a / b
        return answer
    except ZeroDivisionError:
        return None
    except Exception:
        return None
    finally:
        print("inside result: {}".format(answer))
