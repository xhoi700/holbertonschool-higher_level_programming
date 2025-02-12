#!/usr/bin/python3

""" module that creates an obj to file"""

import json


def load_from_json_file(filename):
    """funct that performs the task"""
    with open(filename, "r") as f:
        content = json.load(f)
        return content
