#!/usr/bin/python3
"""Recieves json object from server"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        obj = response.json()
        if not obj:
            print("No result")
        else:
            print(f"{[obj['id']]} {obj['name']}")
    except Exception as invalid:
        print("Not a valid JSON")
