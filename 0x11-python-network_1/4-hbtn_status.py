#!/usr/bin/python3
"""Using request module to fetch a url"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    response = response.text
    resp_type = type(response)
    print("Body response:")
    print(f"\t- type: {resp_type}")
    print(f"\t- content: {response}")
