#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)"""
"""


if __name__ == "__main__":
import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
