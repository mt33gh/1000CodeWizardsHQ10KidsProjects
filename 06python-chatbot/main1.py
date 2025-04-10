"""
What to do:
1. Remove the initial explanation.
2. Learn `random.choice()`
    myList = [1,3,5,7,9,11]
    c = choice(myList)
    print("c =", c)
3. Reduce the long welcome_message to one line of message.
4. Learn `while True:`, which is an infinate loop.
  How can you get out of the loop?
  ==> Use `break`.
5. `command.startswith()` and `command.strip()` are string methods.
  Learn these methods.
  Note that .strip() removes the leading and trailing characters listed in the parentheses.
    mystring = "How are you?"
    if mystring.startswith("How "):
        mystring = mystring.strip("How u?")
    print(mystring)   
6. Learn the `eval()` function.
    print(eval("2+3/4"))
    print(eval("4+5*8-2**4"))

"""



from random import choice

myList = [1,3,5,7,9,11]
c = choice(myList)
print("c =", c)

mystring = "How are you?"
if mystring.startswith("How "):
    mystring = mystring.strip("How u?")
print(mystring)               # are you?

print(eval("2+3/4"))
print(eval("4+5*8-2**4"))

welcome_message = 'Welcome to the "Python Chatbot" app!'

random_facts = [
    "The eye of an ostrich is bigger than its brain.",
    "A dime has 118 ridges on its edge.",
    "Putting sugar on a cut will make it heal faster.",
    "Sign language has tongue twisters.",
    "The plastic tips of shoelaces are called aglets.",
    "Buttermilk does not contain any butter.",
    "The continental plates move at the same rate that fingernails grow.",
]

print(welcome_message)

while True:
    command = input("Enter your command: ")

    if command == "Tell me your name":
        print("Python Chatbot")
    elif command == "What is the meaning of life?":
        print("Programming!")
    elif command.startswith("Calculate"):
        expression = command.strip("Calculate ")
        result = eval(expression)
        print(f"{expression} = {result}")
    elif command == "Give me a random fact":
        random_fact = choice(random_facts)
        print(random_fact)
    elif command == "Goodbye":
        print("See ya later!")
        break
    else:
        print("Sorry, I don't know that command!")
