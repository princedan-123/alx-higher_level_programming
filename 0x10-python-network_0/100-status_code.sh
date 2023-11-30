#!/bin/bash
# A script that displays only the status code of HTTP response to STDOUT
curl -sI -w "%{http_code}" "$1" -o /dev/null
