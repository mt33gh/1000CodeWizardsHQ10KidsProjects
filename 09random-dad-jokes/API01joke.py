"""
Public API
"""

from urllib.request import urlopen
from json import loads

url = "https://v2.jokeapi.dev/joke/Any"

with urlopen(url) as response:
    joke = loads(response.read())

if "joke" in joke:
    print(joke["joke"])
else:
    print("We don't have any jokes now.  Try it again!")
