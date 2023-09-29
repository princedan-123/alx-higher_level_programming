#!/usr/bin/python3
"""Checks the status code of the HTTP response"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        response =  requests.get(url)
        error =response.status_code
        if error < 400:
            print(response.text)
        else:
            print("Error code:", error)
