#!/usr/bin/python3
""" doc """
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    data = response.json()

    i = 0

    for item in list(data):
        if i == 10:
            break
        print(f"{item['sha']}:", item['commit']['committer']['name'])
        i += 1
