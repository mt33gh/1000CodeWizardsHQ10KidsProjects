"""
Public API
"""

from urllib.request import urlopen
from json import loads
import requests

url = "https://uselessfacts.jsph.pl/random.json?language=en"
response = requests.get(url)
fact = response.json()

print(fact["text"])

