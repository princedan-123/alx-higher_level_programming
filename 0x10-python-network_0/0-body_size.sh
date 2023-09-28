#!/bin/bash
# A bash script that displays the size of the response body
curl -Is "$1" |  grep -i Content-Length | grep -oE '[0-9]+'
