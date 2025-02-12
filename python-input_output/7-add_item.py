#!/usr/bin/python3
import os
from sys import argv

"""Imports functions from external scripts to save and load JSON data"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

the_list = []  

if os.path.exists("add_item.json"):
    the_list = load_from_json_file("add_item.json")  
for n in range(1, len(argv)):
    the_list.append(argv[n])
save_to_json_file(the_list, "add_item.json")
