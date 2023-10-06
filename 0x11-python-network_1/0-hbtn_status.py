#!/usr/bin/python3

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    html_bytes = response.read()
    html_str = html_bytes.decode('utf-8')

print("Body response:")
print("\t- type:", type(html_bytes))
print("\t- content:", html_bytes)
print("\t- utf8 content:", html_str)
