#!/usr/bin/python3
"""add item"""


import json
from sys import argv
import os.path

save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(filename):
    obj = load_from_json(filename)
else:
    obj = []
count = 0
fro item in argv:
    if count != 0:
        obj.append(item)
    count += 1
save_to_json(obj, filename)
