#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    
# Get the URL from the command line argument
url = sys.argv[1]

# Send a request to the URL and retrieve the response
with urllib.request.urlopen(url) as response:
    # Extract the value of the X-Request-Id header
    x_request_id = response.getheader('X-Request-Id')
    
    # Display the value of the X-Request-Id header
    print(f"X-Request-Id value: {x_request_id}")