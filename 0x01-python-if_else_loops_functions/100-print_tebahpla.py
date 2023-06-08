#!/usr/bin/python3
# displays the alphabets in reverse order with alternating upper and lowercase
for i in range(122, 97, -2):
    print("{}{}".format(chr(i), chr((i - 1) - 32)), end="")
