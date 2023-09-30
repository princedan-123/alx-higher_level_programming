#!/usr/bin/python3
"""Sends a get request and fetches a variable from the header"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        response = requests.get(url)
        header = response.headers
        value = header.get("X-Request-Id")
        print(value)
