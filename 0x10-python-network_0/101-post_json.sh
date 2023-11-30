#!/bin/bash
# A script that posts a json data to a server
curl -s "$1" -d@"$2" -H "Content-Type: application/json"
