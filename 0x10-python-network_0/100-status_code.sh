#!/bin/bash
# extracts the status code of a HTTP response
curl -sI  -o /dev/null "$1" -w "%{http_code}"
