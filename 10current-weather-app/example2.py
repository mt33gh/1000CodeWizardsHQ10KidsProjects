"""
This program is an example of "urllib.parse.urlencode()".
It converts a Python dictionary to a query string.
"""

import urllib.parse

# Dictionary of parameters
params = {
    "search": "python urllib",
    "page": 1,
    "lang": "en"
}

# Encode parameters into a query string
query_string = urllib.parse.urlencode(params)

# Example URL
base_url = "https://www.example.com/search"

# Full URL with query string
full_url = base_url + "?" + query_string

print(full_url)
