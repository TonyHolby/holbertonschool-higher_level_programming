#!/usr/bin/python3
""" A script that adds all arguments to a list, and save them to a file."""
import sys
import os
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    item_added = load_from_json_file(filename)
except (FileNotFoundError, json.JSONDecodeError):
    item_added = []
item_added.extend(sys.argv[1:])
save_to_json_file(item_added, filename)
