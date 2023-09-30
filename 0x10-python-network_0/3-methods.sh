#!/bin/bash
# Checks for the availaible method allowed on a resource
curl -X HEAD -sI "$1" | grep -i '^Allow:' | sed 's/Allow: //i'
