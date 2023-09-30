#!/usr/bin/python3
"""Using request module to send data"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        data = {"email": email}
        response = requests.post(url, data)
        print(response.text)
