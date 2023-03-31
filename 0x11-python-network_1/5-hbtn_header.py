#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays
 the value of the variable X-Request-Id in the response header
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]  # Get the URL from command line arguments

    response = requests.get(url)  # Send a GET request to the URL
    x_request_id = response.headers.get('X-Request-Id')  # Get the value of the X-Request-Id variable from the response header

    print('X-Request-Id:', x_request_id)  # Print the value of the X-Request-Id variable

    