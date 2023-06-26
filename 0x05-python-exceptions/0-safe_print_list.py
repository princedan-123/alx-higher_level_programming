#!/usr/bin/python3
# Write a function that prints x elements of a list.
def safe_print_list(my_list=[], x=0):
    count = 0
    while count <= x:
        try:
            if count == x:
                break
            print(my_list[count], end="")
            count += 1
        except Exception as e:
            pass
    print("\n")
    return count
