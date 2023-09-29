#!/bin/bash
# Sending a post request using curl
curl -X POST "$1" -s -d "email=test@gmail.com&subject=I will always be here for PLD"
