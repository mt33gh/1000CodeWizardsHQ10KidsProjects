#6(1)Using urllib.request (Built-in)

import urllib.request
import json

url = "https://uselessfacts.jsph.pl/random.json?language=en"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

print("6(1)\n", data["text"])  # Extract and print the fact

#6(2)Using requests (Recommended)

import requests

url = "https://uselessfacts.jsph.pl/random.json?language=en"

response = requests.get(url)  # Send a GET request to the API
data = response.json()  # Convert the response to JSON

print("6(2)\n", data["text"])  # Extract and print the fact