#!/usr/bin/python3

""" module that saves an obj to file"""

import json


def save_to_json_file(my_obj, filename):
    """funct that performs the task"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
