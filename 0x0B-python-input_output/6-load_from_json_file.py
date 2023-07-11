#!/usr/bin/python3
"""import json"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”"""

    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
