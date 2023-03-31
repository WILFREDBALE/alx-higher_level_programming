#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
import urllib.request
import urllib.parse
import sys

# get email and url from command line arguments
email = sys.argv[1]
url = sys.argv[2]

# encode email for use in POST request
data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')

# send POST request and get response
with urllib.request.urlopen(url, data) as response:
    # decode response body in utf-8 and print it
    print(response.read().decode('utf-8'))
