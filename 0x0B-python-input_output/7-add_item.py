#!/usr/bin/python3
"""
    Script that adds all arguments to a Python list.
    and then save them to a file.
"""


import sys
import json
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

new_file = "add_item.json"
new_list = []

if os.path.exists(new_file):
    new_list = load_from_json_file(new_file)

for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])

save_to_json_file(new_list, new_file)
