#!/usr/bin/python3
"""A script that opens a TCP connection to a url and prints its content"""

from urllib.request import urlopen

with urlopen("https://alx-intranet.hbtn.io/status") as response:
    response = response.read()
    print("type: {}".format(type(response)))
    print("content: {}".format(response))
    print("utf8 content: {}".format(response.decode("utf-8")))
