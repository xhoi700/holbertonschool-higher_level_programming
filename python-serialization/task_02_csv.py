#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode="r", encoding="UTF8", newline="") as f:
            csv_data = csv.DictReader(f)
            data = [row for row in csv_data]

        with open("data.json", "w", encoding="UTF8") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        return False
    return True
