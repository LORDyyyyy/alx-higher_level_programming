#!/usr/bin/python3
""" doc """
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    auth = (sys.argv[1], sys.argv[2])

    response = requests.get(url, auth=auth)
    user_data = response.json()
    print(user_data['id'])
