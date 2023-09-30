#!/usr/bin/python3
"""Authenticating through git API"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username =  sys.argv[1]
        password = sys.argv[2]
        url = "http://api.github.com/authorizations"
        data = {
                "username" : username,
                "password" : password
                }
        with requests.post(url, data=data) as response:
            try:
                obj = response.json()
                print(f"{obj['id']}")
            except Exception as error:
                print("None")
