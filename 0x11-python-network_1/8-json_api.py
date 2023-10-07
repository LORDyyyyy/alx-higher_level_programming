#!/usr/bin/python3
""" doc """
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': q})

    try:
        json_data = response.json()

        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
