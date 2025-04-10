
# This program is different from the original randam-dad-jokes.  
# Since the API used in the original program does not work, I have changed 
# APIs.  In addition, I added another API to display a dog picture.

# Base URL: https://v2.jokeapi.dev
# Endpoint: /joke/Any?blacklistFlags=religious,racist,sexist,explicit&type=twopart

from urllib.request import urlopen
from json import loads
import webbrowser

def get_random_joke():
    BASE_URL = "https://v2.jokeapi.dev"
    endpoint = "/joke/Any?blacklistFlags=religious,racist,sexist,explicit&type=twopart"      
    request_url = f"{BASE_URL}{endpoint}"
    with urlopen(request_url) as response:
        joke = loads(response.read())
    return joke

def display_joke(joke):
    category = joke["category"].upper()
    setup = joke["setup"]
    punchline = joke["delivery"]
    print(f"CATEGORY:  {category}")
    print(f"SETUP:     {setup}")
    input("[Press `Enter` to hear the punchline...]")    
    print(f"PUNCHLINE: {punchline}")
   
welcome_message = """
    Welcome to the `Jokes and Dogs` app!

    This app uses an API to fetch a random setup
    and punchline to a joke. The setup will
    be displayed to you, and when you press `Enter`,
    you'll be shown the punchline.
"""

options = """
    (1) Get Dad Joke (2) Exit
"""

GET_JOKE = 1
EXIT = 2

while True:
    user_choice = int(input(options))

    if user_choice == GET_JOKE:
        random_joke = get_random_joke()
        display_joke(random_joke)
    elif user_choice == EXIT:
        break
