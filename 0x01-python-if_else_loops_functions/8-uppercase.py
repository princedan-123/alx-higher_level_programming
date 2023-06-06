#!/usr/bin/python3
def uppercase(str):
    strlen = len(str)
    for i in range(0,strlen):
        asci = ord(str[i])
        print("{}".format(chr(asci - 32)))
    print("\n")
