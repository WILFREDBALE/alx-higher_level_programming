#!/bin/bash

# Get the URL from the user
read -p "Enter a URL: " url

# Send a request to the URL and save the response to a temporary file
response=$(curl -s -w "%{size_download}" -o /dev/null $url)

# Display the size of the response body
echo "The size of the response body is $response bytes."
