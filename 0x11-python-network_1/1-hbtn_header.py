#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
