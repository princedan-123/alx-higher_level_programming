#!/bin/bash
# Checks for the availaible method allowed on a resource
curl -X OPTION -sI "$1" | grep -i '^Allow:' | sed 's/Allow: //i'
