#!/usr/bin/python3
"""Post an email to a server"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        data = {"email": email}
        value = urllib.parse.urlencode(data).encode("utf-8")
        request_object = urllib.request.Request(url, value)
        try:
            with urllib.request.urlopen(request_object) as response:
                response_body = response.read()
                response_string = response_body.decode("utf-8")
                print(response_string)
        except Exception as e:
            print(e)
