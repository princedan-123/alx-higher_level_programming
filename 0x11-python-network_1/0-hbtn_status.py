#!/usr/bin/python3
"""Sending a get request to a server"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        response = r.read()
        obj_type = type(response)
        utf8 = response.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(obj_type))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(utf8))
