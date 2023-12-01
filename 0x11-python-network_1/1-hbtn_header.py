#!/usr/bin/python3
"""A script that takes a url, sends a request and prints a header."""
from urllib.request import urlopen
import sys

url = sys.argv[1]
with urlopen(url) as response:
    headers =  response.headers
    id_header = headers.get("X-Request-Id")
    print(id_header)
