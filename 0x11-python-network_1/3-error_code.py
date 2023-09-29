#!/usr/bin/python3
"""Handling HTTPError"""

import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        try:
            with urllib.request.urlopen(url) as response:
                body = response.read().decode("utf-8")
                print(body)
        except urllib.error.HTTPError as error:
            print("Error code:", error.code)
