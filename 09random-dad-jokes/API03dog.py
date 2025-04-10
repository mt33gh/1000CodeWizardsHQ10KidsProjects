"""
Public API
"""

from urllib.request import urlopen
from json import loads
import webbrowser

url = "https://dog.ceo/api/breeds/image/random"
with urlopen(url) as response:
    dog = loads(response.read())
print(dog["message"])  # URL of a random dog image

import webbrowser
webbrowser.open(dog["message"])  # Opens in default browser
