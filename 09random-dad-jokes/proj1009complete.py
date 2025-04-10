"""
What to do:
1. Learn about urllib.request.urlopn at:
  https://docs.python.org/3/library/urllib.request.html
2. Learn about the "with" statement at:
  https://builtin.com/software-engineering-perspectives/what-is-with-statement-python




"""

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
   #endpoint = "/joke/Any?blacklistFlags=religious,racist,sexist,explicit&type=single"
    endpoint = "/joke/Any?blacklistFlags=religious,racist,sexist,explicit&type=twopart"
        
    request_url = f"{BASE_URL}{endpoint}"
    print("request_url=", request_url)
    with urlopen(request_url) as response:
        joke = loads(response.read())
    return joke

def display_joke(joke):
    category = joke["category"].upper()
    setup = joke["setup"]
    punchline = joke["delivery"]
    print(f"CATEGORY:  {category}.")
    print(f"SETUP:     {setup}")
    your_guess = input("[Press `Enter` to hear the punchline...]")    
    if your_guess in punchline:
        print("You are right about this joke!")    
    print(f"PUNCHLINE: {punchline}")
    #print(joke)

def get_dog():
    BASE_URL = "https://dog.ceo"
    endpoint = "/api/breeds/image/random"     
    request_url = f"{BASE_URL}{endpoint}"
    print("request_url=", request_url)
    with urlopen(request_url) as response:
        dog = loads(response.read())
    return dog

def display_dog(dog_pic):
    print(dog_pic["message"])   # prints the URL of dog_pic
    webbrowser.open(dog_pic["message"])  # Opens in default browser
    
welcome_message = """
    Welcome to the `Jokes and Dogs` app!

    This app uses an API to fetch a random setup
    and punchline to a joke. The setup will
    be displayed to you, and when you press `Enter`,
    you'll be shown the punchline.
"""

options = """
    (1) Get Dad Joke (2) See Dogs (3) Exit
"""

GET_JOKE = 1
SEE_DOGS = 2
EXIT = 3

while True:
    user_choice = int(input(options))

    if user_choice == GET_JOKE:
        random_joke = get_random_joke()
        display_joke(random_joke)
    elif user_choice == SEE_DOGS:
        dog_picture = get_dog()
        display_dog(dog_picture)
    elif user_choice == EXIT:
        break
