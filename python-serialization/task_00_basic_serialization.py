#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a Python dictionary."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
