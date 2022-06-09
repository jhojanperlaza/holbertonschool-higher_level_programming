#!/usr/bin/python3
"""

script that adds all
arguments to a Python
list, and then save
them to a file:

"""
from os.path import exists
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


file_name = "add_item.json"
if exists("add_item.json") is not True:
    list_json = []
    save_to_json_file(list_json, file_name)
list_json = load_from_json_file(file_name)

for argv in sys.argv[1:]:
    list_json += [argv]

save_to_json_file(list_json, file_name)
