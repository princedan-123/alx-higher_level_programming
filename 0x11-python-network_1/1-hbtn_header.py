#!/usr/bin/python3
"""Fetches a resource from the internet"""

import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        try:
            with urllib.request.urlopen(url) as response:
                header = response.headers
                value = header.get("X-Request-Id")
                print(value)
        except Exception:
            pass
