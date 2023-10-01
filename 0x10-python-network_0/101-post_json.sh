#!/bin/bash
# Sends a post request using data from a file
curl -X POST -d @"$2" -s "$1" -H "Content-Type: application/json"
