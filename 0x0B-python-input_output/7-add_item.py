#!/usr/bin/python3
"""this script takes command line argument and saves it to a file"""
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
from sys import argv


with open("add_item.json", "w") as f:
    save_to_json_file(argv[1:], "add_item.json")
